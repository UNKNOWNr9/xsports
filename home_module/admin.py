from django.contrib import admin

from .models import ComingSoon


@admin.register(ComingSoon)
class ComingSoonAdmin(admin.ModelAdmin):
    list_display = ['email', ]
