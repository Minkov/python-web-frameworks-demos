from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("qna_demos.web.urls")),
    path("api/", include("qna_demos.api.urls")),
]
