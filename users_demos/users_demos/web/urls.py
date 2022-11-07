from django.urls import path

from users_demos.auth_app.views import SignUpView
from users_demos.web.views import UsersListView

urlpatterns = (
    path('', UsersListView.as_view(), name='index'),
)
