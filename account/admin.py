from django.contrib import admin

from .models import Profile


admin.site.site_header = "Jatyam"


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'fullname']


admin.site.register(Profile, ProfileAdmin)
