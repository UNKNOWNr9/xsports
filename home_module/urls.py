from django.urls import path
from .views import Index, Complete

urlpatterns = [
    path('', Index.as_view()),
    path('s/', Complete.as_view()),
]
