from django.urls import path

from todos_app_workshop.todos.views import TodoListCreateApiView, CategoriesListApiView, TodoDetailsUpdateApiView

urlpatterns = (
    path("", TodoListCreateApiView.as_view(), name="api_list_create_todos"),
    path("<int:pk>/", TodoDetailsUpdateApiView.as_view(), name="api_details_todo"),
    path("categories/", CategoriesListApiView.as_view(), name="api_list_categories"),
)
