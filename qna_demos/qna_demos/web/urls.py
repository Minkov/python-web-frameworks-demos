from django.urls import path

from qna_demos.web.views import IndexView, CreateTodoView

urlpatterns = (
    path("", IndexView.as_view(), name="index"),
    path("todo/create/", CreateTodoView.as_view(), name="create_todo"),
)
