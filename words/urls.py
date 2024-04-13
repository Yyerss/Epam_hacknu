from django.urls import path
from .views import RememberWordView, RandomWordView

urlpatterns = [
    path('remember-word/', RememberWordView.as_view(), name='remember-word'),
    path('api/v1/random-word/', RandomWordView.as_view(), name='random-word'),
]
