from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Employee(models.Model):
    first_name = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=15,
        null=True,
        blank=True,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
