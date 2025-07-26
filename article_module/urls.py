from django.urls import path
from .views import ArticleListView, ArticleDetailView, article_by_category, article_by_author

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('category/<slug:slug>/', article_by_category, name='article_by_category'),
    path('author/<str:username>/', article_by_author, name='article_by_author'),
]