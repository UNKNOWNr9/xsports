from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_module.urls')),
    path('article/', include('article_module.urls')),
]
