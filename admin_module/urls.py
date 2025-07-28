from django.urls import path
from .views import ProfileView, EditProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),
]