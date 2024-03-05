from django.urls import path

from users_demos.web.views import index, about, TeamView

urlpatterns = (
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("team/", TeamView.as_view(), name="team"),
)
