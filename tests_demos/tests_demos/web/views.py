from django import forms
from django.views import generic as views
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth import mixins as auth_mixins

UserModel = get_user_model()


def show_users(request):
    users_list = UserModel.objects.all()
    context = {
        "user_list": users_list,
    }

    return render(request, "users.html", context)


class ListUsersView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = "users.html"

    ordering = ["-date_joined"]

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.order_by("-date_joined")
    #     return queryset
