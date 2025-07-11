from django.contrib import admin
from .models import Article, ArticleCategory


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date', 'is_active', 'author', 'selected_category']
    list_editable = ['is_active',]


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
