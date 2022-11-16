from django.contrib import admin

from testing_demos.web.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
