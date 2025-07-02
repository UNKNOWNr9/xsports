from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'home_module/index.html'


class Complete(TemplateView):
    template_name = 'home_module/complete.html'
