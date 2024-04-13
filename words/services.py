from .models import CustomUser, UserWord
from django.utils import timezone


def calculate_language_level(user):
    user_words = UserWord.objects.filter(user=user, remembered=True)
    score = 0
    for user_word in user_words:
        difficulty_weight = {'E': 1, 'M': 2, 'H': 3}[user_word.word.difficulty]
        time_since_review = (timezone.now() - user_word.last_reviewed).days
        review_factor = min(user_word.review_count, 5)
        score += difficulty_weight * review_factor / max(1, time_since_review)

    levels = [(50, 'A1'), (100, 'A2'), (200, 'B1'), (300, 'B2'), (400, 'C1'), (500, 'C2')]
    new_level = next((level for points, level in reversed(levels) if score >= points), 'A1')

    if new_level != user.language_level:
        user.language_level = new_level
        user.save()