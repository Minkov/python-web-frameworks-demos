from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path("admin/", admin.site.urls),
    path("", include("custom_auth_demos.web.urls")),
    path("accounts/", include("custom_auth_demos.accounts.urls")),

    # Almost same as:
    # path("accounts/login/", LoginUserView.as_view(), name="login_user"),
    # path("accounts/register/", RegisterUserView.as_view(), name="register_user"),
)
