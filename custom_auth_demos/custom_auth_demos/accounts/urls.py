from django.urls import path

from custom_auth_demos.accounts.views import LoginUserView, RegisterUserView

urlpatterns = (
    path("login/", LoginUserView.as_view(), name="login_user"),
    path("register/", RegisterUserView.as_view(), name="register_user"),
)
