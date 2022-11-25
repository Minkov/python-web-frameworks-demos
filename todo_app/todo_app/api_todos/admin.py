from django.contrib import admin

from todo_app.api_todos.models import Todo, Category


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
