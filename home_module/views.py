from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.views.generic import View

from article_module.models import Article
from .forms import ComingSoonForm
from .models import ComingSoon


class HomeView(ListView):
    template_name = 'home_module/index.html'
    model = Article
    paginate_by = 6
    context_object_name = 'article'

    def get_queryset(self):
        return Article.objects.published().order_by('-create_date')


def footer_component_view(request):
    return render(request, 'shared/site_footer_component.html')


def header_component_view(request):
    return render(request, 'shared/site_header_component.html')


class ComingSoonView(View):
    def get(self, request):
        coming_soon_form = ComingSoonForm()
        context = {
            'coming_soon_form': coming_soon_form
        }
        return render(request, 'home_module/coming_soon.html', context)

    def post(self, request):
        coming_soon_form = ComingSoonForm(request.POST)
        if coming_soon_form.is_valid():
            user_email = coming_soon_form.cleaned_data.get('email')
            if ComingSoon.objects.filter(email=user_email).exists():
                messages.warning(request, '.این ایمیل قبلاً ثبت شده است. نیازی به ثبت دوباره وجود ندارد')
                return redirect(reverse('coming_soon'))
            ComingSoon.objects.create(email=user_email)
            messages.success(request, '.ایمیل شما با موفقیت ثبت شد و در صورت باز شدن فروشگاه به شما اطلاع داده می‌شود')
            return redirect(reverse('coming_soon'))
        context = {
            'coming_soon_form': coming_soon_form
        }
        return render(request, 'home_module/coming_soon.html', context)
