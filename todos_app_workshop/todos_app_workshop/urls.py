from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include([
        path("auth/", include("todos_app_workshop.todos_auth.urls")),
        path("todos/", include("todos_app_workshop.todos.urls")),
    ])),
]
