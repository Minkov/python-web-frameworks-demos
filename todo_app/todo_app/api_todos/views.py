from rest_framework import generics as rest_generic_views, permissions, exceptions as rest_exceptions

from todo_app.api_todos.models import Todo, Category
from todo_app.api_todos.serializers import CategorySerializer, TodoForCreateSerializer, TodoForListSerializer, \
    TodoForDetailsSerializer


class ListCreateTodoApiView(rest_generic_views.ListCreateAPIView):
    queryset = Todo.objects.all()

    create_serializer_class = TodoForCreateSerializer
    list_serializer_class = TodoForListSerializer
    filter_names = ('category',)

    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.create_serializer_class

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)

        return self.__apply_filters_to_queryset(queryset)

    def __apply_filters_to_queryset(self, queryset):
        queryset_params = {}
        for filter_name in self.filter_names:
            filter_id = self.request.query_params.get(filter_name, None)
            if filter_id:
                queryset_params[f'{filter_name}'] = filter_id

        return queryset.filter(**queryset_params)


class DetailsTodoApiView(rest_generic_views.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoForDetailsSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_object(self):
        todo = super().get_object()

        if todo.user != self.request.user:
            raise rest_exceptions.PermissionDenied

        return todo


class ListCategoriesApiView(rest_generic_views.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        return self.queryset\
            .filter(todo__user_id=self.request.user.id)\
            .distinct()
