from django.contrib import admin
from .models import CostumeUser


@admin.register(CostumeUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'about_user']