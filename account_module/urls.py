from django.urls import path
from .views import RegisterView, ActivateAccountView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('activate_account/<email_active_code>/', ActivateAccountView.as_view(), name='activate'),
]