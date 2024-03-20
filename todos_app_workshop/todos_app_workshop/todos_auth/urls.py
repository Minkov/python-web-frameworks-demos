from django.urls import path

from todos_app_workshop.todos_auth.views import CreateUserApiView, LoginApiView

urlpatterns = (
    path("register/", CreateUserApiView.as_view(), name="api_create_user"),
    path("login/", LoginApiView.as_view(), name="api_login_user"),
)
