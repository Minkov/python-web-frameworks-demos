from django.db import models


class Model1(models.Model):
    title = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )


class Model2(models.Model):
    pass
