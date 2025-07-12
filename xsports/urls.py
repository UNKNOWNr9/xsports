from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_module.urls')),
    path('article/', include('article_module.urls')),
    path('account/', include('account_module.urls')),
    path('contact/', include('contact_module.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
