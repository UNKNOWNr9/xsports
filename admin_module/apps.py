from django.apps import AppConfig


class AdminModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_module'
    verbose_name = 'ادمین پنل'
    verbose_name_plural = 'ادمین پنل'
