from django.contrib import admin
from contact_module.models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'subject', 'phone']