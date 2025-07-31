from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, reverse, Http404
from django.views.generic import View, ListView, DeleteView, UpdateView
from .forms import EditProfileForm, ChangePasswordForm
from account_module.models import CustomUser
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import ArticleForm
from .mixins import AuthorRequiredMixin
from article_module.models import Article
from django.urls import reverse_lazy


class ProfileView(LoginRequiredMixin, View):
    template_name = 'admin_module/profile.html'
    login_url = 'login'

    def get(self, request):
        user = request.user
        edit_profile_form = EditProfileForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'about_user': user.about_user,
        })
        context = {
            'edit_profile_form': edit_profile_form,
            'user': user,
        }
        return render(request, 'admin_module/profile.html', context)

    def post(self, request):
        user = request.user
        edit_profile_form = EditProfileForm(request.POST, request.FILES)
        if edit_profile_form.is_valid():
            user.first_name = edit_profile_form.cleaned_data.get('first_name')
            user.last_name = edit_profile_form.cleaned_data.get('last_name')
            user.about_user = edit_profile_form.cleaned_data.get('about_user')
            user.avatar = edit_profile_form.cleaned_data.get('avatar')
            user.save()
            return redirect('profile')
        context = {
            'edit_profile_form': edit_profile_form
        }
        return render(request, 'admin_module/profile.html', context)


class ChangePasswordView(LoginRequiredMixin, View):
    def get(self, request):
        change_password_form = ChangePasswordForm
        context = {
            'change_password_form': change_password_form
        }
        return render(request, 'admin_module/change_password.html', context)

    def post(self, request):
        user: CustomUser = request.user
        change_password_form = ChangePasswordForm(request.POST)
        if change_password_form.is_valid():
            old_password = change_password_form.cleaned_data.get('old_password')
            new_password = change_password_form.cleaned_data.get('new_password')
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                messages.success(request, 'رمز عبور شما با موفقیت تغییر کرد!')
                update_session_auth_hash(request, user)
                return redirect(reverse('change_password'))
            else:
                change_password_form.add_error('old_password', 'رمز عبور فعلی نادرست است.')

        context = {
            'change_password_form': change_password_form
        }
        return render(request, 'admin_module/change_password.html', context)


class AddArticleView(AuthorRequiredMixin, View):
    def get(self, request):
        form = ArticleForm()
        return render(request, 'admin_module/add_article.html', {'form': form})

    def post(self, request):
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            # TODO: redirect to my posts
            return redirect('add_article')
        return render(request, 'admin_module/add_article.html', {'form': form})


class PublishedPostsView(AuthorRequiredMixin, ListView):
    model = Article
    template_name = 'admin_module/published_posts.html'

    def get_queryset(self):
        return Article.objects.published().filter(author=self.request.user).order_by('-create_date')


class DraftPostsView(AuthorRequiredMixin, ListView):
    model = Article
    template_name = 'admin_module/draft_posts.html'

    def get_queryset(self):
        return Article.objects.draft().filter(author=self.request.user).order_by('-create_date')


class RejectedPostsView(AuthorRequiredMixin, ListView):
    model = Article
    template_name = 'admin_module/rejected_posts.html'

    def get_queryset(self):
        return Article.objects.rejected().filter(author=self.request.user).order_by('-create_date')


class InvestigationPostsView(AuthorRequiredMixin, ListView):
    model = Article
    template_name = 'admin_module/investigation_posts.html'

    def get_queryset(self):
        return Article.objects.investigation().filter(author=self.request.user)


class EditArticleView(AuthorRequiredMixin, UpdateView):
    model = Article
    template_name = 'admin_module/edit_article.html'
    form_class = ArticleForm
    success_url = reverse_lazy('published_posts')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise Http404("دسترسی غیرمجاز")
        if obj.status == 'published':
            raise Http404("پست منتشر شده قابل ویرایش نیست.")
        return obj


class ArticleDeleteView(AuthorRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'admin_module/published_posts.html'
    model = Article
    success_url = reverse_lazy('published_posts')

    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user
