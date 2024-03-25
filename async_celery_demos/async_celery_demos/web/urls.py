from django.urls import path

from async_celery_demos.web.views import index

urlpatterns = [
    path("", index, name="index"),
]
