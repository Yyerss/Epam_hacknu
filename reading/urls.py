# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('reading/<int:pk>/', ReadingAPIView.as_view(), name='reading-detail'),
]