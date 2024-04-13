from django.db.models import Sum, F, FloatField
from .models import *


def calculate_language_level(submission):
    correct_answers = submission.answers.filter(is_correct=True).count()
    total_questions = Question.objects.count()
    score = correct_answers / total_questions

    if score > 0.9:
        level = 'C2'
    elif score > 0.75:
        level = 'C1'
    elif score > 0.6:
        level = 'B2'
    elif score > 0.45:
        level = 'B1'
    elif score > 0.3:
        level = 'A2'
    else:
        level = 'A1'

    submission.user.language_level = level
    submission.user.save()