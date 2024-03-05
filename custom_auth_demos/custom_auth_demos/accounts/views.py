from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views import generic as views

from custom_auth_demos.accounts.forms import AccountUserCreationForm


class LoginUserView(auth_views.LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("index")


class RegisterUserView(views.CreateView):
    form_class = AccountUserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("index")
