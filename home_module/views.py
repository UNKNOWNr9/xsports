from django.views.generic import TemplateView
from django.shortcuts import render


class HomeView(TemplateView):
    template_name = 'home_module/index.html'


def footer_component_view(request):
    return render(request, 'shared/site_footer_component.html')


def header_component_view(request):
    return render(request, 'shared/site_header_component.html')
