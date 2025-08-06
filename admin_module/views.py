from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, reverse, Http404
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DeleteView, UpdateView

from account_module.models import CustomUser
from article_module.models import Article
from .forms import ArticleForm, AuthorRequestForm
from .forms import EditProfileForm, ChangePasswordForm
from .mixins import AuthorRequiredMixin
from .models import AuthorRequest


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
            return redirect('draft_posts')
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
    success_url = reverse_lazy('draft_posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.status == 'RJ':
            context['rejection_reason'] = self.object.rejected_reason
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise Http404("دسترسی غیرمجاز")
        if obj.status == 'PB' or obj.status == 'IN':
            raise Http404("پست ارسال شده و قابل ادیت نیست")
        return obj

    def form_valid(self, form):
        article = form.save(commit=False)

        if 'send_for_review' in self.request.POST:
            article.status = 'IN'
        else:
            article.status = 'DF'

        article.save()
        return super().form_valid(form)


class ArticleDeleteView(AuthorRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'admin_module/published_posts.html'
    model = Article
    success_url = reverse_lazy('published_posts')

    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user


class AuthorRequestView(LoginRequiredMixin, View):
    login_url = '/account/login/'

    def get(self, request):
        author_request_form = AuthorRequestForm()
        context = {
            'author_request_form': author_request_form
        }
        return render(request, 'admin_module/author-request.html', context)

    def post(self, request):
        if AuthorRequest.objects.filter(email=request.user.email).exists():
            messages.error(request,
                           'شما قبلاً درخواست نویسندگی ثبت کرده‌اید. رزومه شما در حال بررسی می‌باشد. از صبر و شکیبایی شما سپاسگزاریم.')
            return redirect('author_request')

        author_request_form = AuthorRequestForm(request.POST)
        if author_request_form.is_valid():
            author_request = author_request_form.save(commit=False)
            author_request.email = request.user.email
            author_request.save()
            messages.success(request,
                             'درخواست شما با موفقیت ثبت شد. طی یک هفته بررسی خواهد شد و با شما تماس گرفته می‌شود.')
            return redirect('author_request')

        context = {
            'author_request_form': author_request_form
        }
        return render(request, 'admin_module/author-request.html', context)
