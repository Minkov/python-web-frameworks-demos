from django.contrib import admin

from custom_auth_demos.web.models import Model1


@admin.register(Model1)
class Model1Admin(admin.ModelAdmin):
    pass
