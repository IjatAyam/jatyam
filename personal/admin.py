from django.contrib import admin

from .models import HomeSlider


class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']
    ordering = ['order']


admin.site.register(HomeSlider, HomeSliderAdmin)
