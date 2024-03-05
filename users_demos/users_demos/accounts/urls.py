from django.urls import path

from users_demos.accounts.views import LoginUserView, RegisterUserView

urlpatterns = (
    path("login/", LoginUserView.as_view(), name="login-user"),
    path("register/", RegisterUserView.as_view(), name="register-user"),
)
