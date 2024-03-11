from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    pass


class ProfileImage(models.Model):
    image = models.ImageField(upload_to='profiles')

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
