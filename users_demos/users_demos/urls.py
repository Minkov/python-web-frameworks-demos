from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users_demos.web.urls")),
    path("accounts2/", include("users_demos.accounts.urls")),
]
