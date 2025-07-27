from django.urls import path
from .views import AdminLteView

urlpatterns = [
    path('', AdminLteView.as_view(), name='dashboard')
]
