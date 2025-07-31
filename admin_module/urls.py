from django.urls import path
from .views import ProfileView, ChangePasswordView, AddArticleView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('add-article/', AddArticleView.as_view(), name='add_article'),
]
