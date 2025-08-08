from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.shortcuts import render


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_module.urls')),
    path('article/', include('article_module.urls')),
    path('account/', include('account_module.urls')),
    path('contact/', include('contact_module.urls')),
    path('dashboard/', include('admin_module.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


def custom_page_not_found_view(request, exception):
    return render(request, "shared/404.html", status=404)


handler404 = custom_page_not_found_view