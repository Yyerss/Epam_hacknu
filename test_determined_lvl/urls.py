from django.urls import path
from .views import QuestionListView, TestSubmissionView

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='questions-list'),
    path('submit-test/', TestSubmissionView.as_view(), name='submit-test'),

]