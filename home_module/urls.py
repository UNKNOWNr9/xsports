from django.urls import path
from .views import HomeView, coming_soon

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('coming-soon', coming_soon, name='coming_soon')
]