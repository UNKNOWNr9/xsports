from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from account_module.models import CustomUser
from .models import Article, ArticleCategory


class ArticleListView(ListView):
    template_name = 'article_module/article_list.html'
    queryset = Article.objects.filter(is_active=True).order_by('-create_date')
    paginate_by = 1


class ArticleDetailView(DetailView):
    template_name = 'article_module/article_detail.html'
    queryset = Article.objects.filter(is_active=True)


def article_sidebar(request):
    latest_articles = Article.objects.filter(is_active=True).order_by('-create_date')
    categories = ArticleCategory.objects.filter(is_active=True)
    context = {
        'latest_artciles': latest_articles,
        'categories': categories,
    }
    return render(request, 'components/sidebar.html', context)


def article_by_category(request, slug):
    category = get_object_or_404(ArticleCategory, slug=slug, is_active=True)
    article = Article.objects.filter(selected_category=category, is_active=True)
    context = {
        'categories': category,
        'articles': article,
    }
    return render(request, 'components/article_by_category.html', context)


def article_by_author(request, username):
    author = get_object_or_404(CustomUser, username=username)
    article = Article.objects.filter(author=author, is_active=True)
    context = {
        'author': author,
        'articles': article
    }
    return render(request, 'components/article_by_author.html', context)