from django.contrib import admin

from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ['order']
    ordering = ['order']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'order', 'published_at']
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ['order']
    ordering = ['order']
    list_filter = ['published_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
