from django.contrib import admin

from .models import ComingSoon, Advertising


@admin.register(ComingSoon)
class ComingSoonAdmin(admin.ModelAdmin):
    list_display = ['email', ]


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ['phone', ]