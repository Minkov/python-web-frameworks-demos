from django.db import models


class DepartmentManager(models.Manager):
    def get_or_create_by_name(self, name):
        try:
            return self.model.objects.filter(name=name) \
                .get()
        except self.model.DoesNotExist:
            return self.model.objects.create(
                name=name,
            )
