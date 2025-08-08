from django.urls import path
from .views import HomeView, ComingSoonView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('coming-soon/', ComingSoonView.as_view(), name='coming_soon'),
]
