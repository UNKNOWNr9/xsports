from django.contrib import messages
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from account_module.models import CustomUser
from .forms import ArticleCommentsForm
from .models import Article, ArticleCategory, ArticleComments


class ArticleListView(ListView):
    template_name = 'article_module/article_list.html'
    queryset = Article.objects.published().order_by('-create_date')
    paginate_by = 3


class ArticleDetailView(DetailView):
    template_name = 'article_module/article_detail.html'
    queryset = Article.objects.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context['comments'] = ArticleComments.objects.filter(article=article, is_active=True)
        context['comment_form'] = ArticleCommentsForm()
        return context

    # comments view
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'برای ارسال نظر باید اول وارد حساب کاربری شوید.')
            return redirect(request.path)
        self.object = self.get_object()
        comment_form = ArticleCommentsForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = self.object
            comment.user = request.user
            comment_form.save()
            messages.success(request, 'کامنت شما ثبت شد، طی 48 ساعت پس از تایید نمایش داده میشود.')
            return redirect(self.request.path_info)
        context = self.get_context_data()
        context['comment_form'] = comment_form
        return redirect(self.request.path_info)


def article_sidebar(request):
    latest_articles = Article.objects.published().order_by('-create_date')
    categories = ArticleCategory.objects.filter(is_active=True).annotate(count=Count('article_category'))
    context = {
        'latest_artciles': latest_articles,
        'categories': categories,
    }
    return render(request, 'components/sidebar.html', context)


def article_by_category(request, slug):
    category = get_object_or_404(ArticleCategory, slug=slug, is_active=True)
    article = Article.objects.published().filter(selected_category=category)
    context = {
        'categories': category,
        'articles': article,
    }
    return render(request, 'components/article_by_category.html', context)


def article_by_author(request, username):
    author = get_object_or_404(CustomUser, username=username)
    article = Article.objects.published().filter(author=author)
    context = {
        'author': author,
        'articles': article
    }
    return render(request, 'components/article_by_author.html', context)
