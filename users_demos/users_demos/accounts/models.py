from django.contrib.auth.models import AnonymousUser
from django.db import models
from django.contrib.auth import models as auth_models


# Just add new fields:
# class AppUser(auth_models.AbstractUser):
#     age = models.PositiveIntegerField()


# Completely replace the User
# class AppUser(AbstractBaseUser, PermissionsMixin):
#     USERNAME_FIELD = "email"
#     pass

# getattr(self, "email")

