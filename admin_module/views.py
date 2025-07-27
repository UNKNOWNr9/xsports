from django.views.generic import TemplateView


class AdminLteView(TemplateView):
    template_name = 'admin_module/index.html'
