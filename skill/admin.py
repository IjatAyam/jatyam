from django.contrib import admin

from .models import Skill, Showcase


class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'percent', 'order']
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ['percent', 'order']
    ordering = ['order']


class ShowcaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'published_at']
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ['order']
    ordering = ['order']
    list_filter = ['published_at']


admin.site.register(Skill, SkillAdmin)
admin.site.register(Showcase, ShowcaseAdmin)
