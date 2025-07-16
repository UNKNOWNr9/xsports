from django.urls import path
from .views import RegisterView, ActivateAccountView, LoginView, ForgotPasswordView, ResetPasswordView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('activate_account/<email_active_code>/', ActivateAccountView.as_view(), name='activate'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password/<email_active_code>/', ResetPasswordView.as_view(), name='reset_password'),
]