from django.apps import AppConfig


class ArticleModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'article_module'
    verbose_name = 'وبلاگ'
    verbose_name_plural = 'وبلاگ'
