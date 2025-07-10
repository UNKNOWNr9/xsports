from django.views.generic import ListView, TemplateView


class ArticleListView(TemplateView):
    template_name = 'article_module/article_list.html'

