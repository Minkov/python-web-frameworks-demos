from django.core.paginator import Paginator
from rest_framework import generics as api_views, serializers, permissions

from todos_app_workshop.todos.models import Todo, Category, TodoState


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TodoBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class TodoListSerializer(TodoBaseSerializer):
    category = CategorySerializer(many=False)


class TodoCreateSerializer(TodoBaseSerializer):
    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)

    class Meta(TodoBaseSerializer.Meta):
        fields = ("title", "description", "category")


class TodoDetailsSerializer(TodoBaseSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)

        return {
            **result,
            "is_done": result["state"] == TodoState.DONE,
        }


class TodoDetailsUpdateApiView(api_views.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    # Usually, `TodoDetailsSerializer`
    serializer_class = TodoDetailsSerializer

    def get_serializer(self, instance, data=None, partial=None):
        if self.request.method == 'PUT':
            data = {
                **data,
                "state": TodoState.DONE if data["is_done"] else TodoState.NOT_DONE,
            }

            return super().get_serializer(instance, data=data, partial=partial)

        return super().get_serializer(instance)


class TodoListCreateApiView(api_views.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Todo.objects.all()

    list_serializer_class = TodoListSerializer
    create_serializer_class = TodoCreateSerializer
    serializer_class = list_serializer_class

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.create_serializer_class

        return self.list_serializer_class

    filter_funcs = [
        "filter_by_user",
        "filter_by_category",
        "filter_by_state",
    ]

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        for filter_func_name in self.filter_funcs:
            filter_func = getattr(self, filter_func_name, None)
            if filter_func:
                queryset = filter_func(queryset)

        return queryset

    def filter_by_user(self, queryset):
        return queryset.filter(user=self.request.user)

    def filter_by_category(self, queryset):
        category_id = self.request.query_params.get('category', None)
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def filter_by_state(self, queryset):
        state = self.request.query_params.get('state', None)
        if state is not None:
            expected_state = TodoState.DONE if state == "true" else TodoState.NOT_DONE
            queryset = queryset.filter(state=expected_state)
        return queryset


class CategoriesListApiView(api_views.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
