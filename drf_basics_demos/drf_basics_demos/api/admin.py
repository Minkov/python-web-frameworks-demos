from django.contrib import admin

from drf_basics_demos.api.models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")
