from django.contrib import admin

from auth_demos.web.models import Model1, Model2


@admin.register(Model1)
class Model1Admin(admin.ModelAdmin):
    pass


@admin.register(Model2)
class Model1Admin(admin.ModelAdmin):
    pass
