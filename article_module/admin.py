from django.contrib import admin

from .models import Article, ArticleCategory, ArticleComments


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date', 'selected_category']


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active', ]


@admin.register(ArticleComments)
class ArticleCommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'created_at']