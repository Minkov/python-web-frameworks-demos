from django.contrib.auth.views import LoginView
from django.urls import path

from tests_demos.web.views import show_users, ListUsersView

urlpatterns = (
    path("", show_users, name="index_fbv"),
    path("cbv/", ListUsersView.as_view(), name="index_cbv"),

    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
)
