from django.urls import path

from todo_app.api_todos.views import ListCreateTodoApiView, ListCategoriesApiView, DetailsTodoApiView

urlpatterns = (
    path('', ListCreateTodoApiView.as_view(), name='api list todos'),
    path('<int:pk>/', DetailsTodoApiView.as_view(), name='api details todo'),
    path('categories/', ListCategoriesApiView.as_view(), name='api list categories'),
)
