from django.urls import path
from .views import ProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', ProfileView.as_view(), name='edit_profile'),
]