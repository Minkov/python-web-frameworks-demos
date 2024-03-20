from django.contrib import admin

from todos_app_workshop.todos.models import Todo, Category


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'state', 'category_name')

    def category_name(self, obj):
        return obj.category.name


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
