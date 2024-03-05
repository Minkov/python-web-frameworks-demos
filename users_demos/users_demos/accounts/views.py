from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import redirect_to_login
from django.views import generic as views
from django.urls import reverse, reverse_lazy

from django.contrib.auth import views as auth_views, get_user_model, forms as auth_forms
from users_demos.accounts.forms import CreateUserForm

# `authenticate(request, **credentials)` -> returns the user if credentials match
# `login(request, user)` -> attaches a cookie for the authenticated user

# The correct way to get the `User` class
UserModel = get_user_model()


# UserModel(...).save()
# UserModel.objects.create(...)


# `doncho4` -> 'pbkdf2_sha256$600000$ovLVt6LZPeU5BiU2HrzPHw$Cn8dXWbgMrQIkYimRQY4AgzyqqrOODHAubtAb7tPUNY='

class LoginUserView(auth_views.LoginView):
    template_name = "accounts/login_user.html"

    # def get_success_url(self):
    #   # return whatever you want
    #   pass


class RegisterUserView(views.CreateView):
    form_class = CreateUserForm
    template_name = "accounts/register_user.html"
    success_url = reverse_lazy("index")

# class LoginUserView(views.View):
#     form_class = auth_forms.AuthenticationForm
#
#     def get(self, request, *args, **kwargs):
#         context = {
#             'form': self.form_class()
#         }
#
#         return render(request, 'accounts/login_user.html', context)
#
#     def post(self, request, *args, **kwargs):
#         # form = self.form_class(request.POST or None)
#         # if form.is_valid():
#         # username, password = request.POST["username"], request.POST["password"]
#         #
#         # user = authenticate(username=username, password=password)
#         # print(user)
#
#         # if user is not None:
#         #     # Add the user to the session
#         #     login(request, user)
#         login(request, User.objects.get(pk=2))
#         return redirect("index")
