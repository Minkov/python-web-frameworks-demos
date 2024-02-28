from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from auth_demos.web.views import index, private_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("", index, name="index"),
    path("private/", private_view, name="private_view"),
]
