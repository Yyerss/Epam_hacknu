from django.urls import path
from .views import DailyGrammarAndWords

urlpatterns = [
    path('api/generate-grammar-words/', DailyGrammarAndWords.as_view(), name='generate-grammar-words'),
]