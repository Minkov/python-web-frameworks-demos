from django.urls import path

from qna_demos.api.views import TodosListView

urlpatterns = (
    path("todos/", TodosListView.as_view(), name="todos-list"),
)
