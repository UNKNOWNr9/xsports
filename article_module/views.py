from django.views.generic import ListView, DetailView
from .models import Article


class ArticleListView(ListView):
    template_name = 'article_module/article_list.html'
    queryset = Article.objects.filter(is_active=True).order_by('-create_date')
    paginate_by = 1



class ArticleDetailView(DetailView):
    template_name = 'article_module/article_detail.html'
    queryset = Article.objects.filter(is_active=True)