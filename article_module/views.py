from django.views.generic import ListView, DetailView
from .models import Article, ArticleCategory
from django.shortcuts import render


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