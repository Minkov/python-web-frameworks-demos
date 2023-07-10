from django.db import models


class Task(models.Model):
    title = models.CharField(
        max_length=15,
    )


# Task.objects.all()