from django.contrib import admin

from drf_basics_demos.api.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre")
