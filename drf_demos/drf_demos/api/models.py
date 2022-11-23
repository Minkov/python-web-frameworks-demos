from django.db import models

from drf_demos.api.managers import DepartmentManager


class Department(models.Model):
    objects = DepartmentManager()

    name = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(
        max_length=30,
    )

    salary = models.PositiveIntegerField()

    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return self.name
