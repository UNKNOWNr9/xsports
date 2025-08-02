from django.contrib import admin
from .models import AuthorRequest


@admin.register(AuthorRequest)
class AuthorRequestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'age']