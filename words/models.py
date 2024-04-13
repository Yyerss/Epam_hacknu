from django.db import models
from custom_auth.models import CustomUser
from django.utils import timezone
# Create your models here.


class Word(models.Model):
    kazakh = models.CharField(max_length=100)
    russian = models.CharField(max_length=100)
    english = models.CharField(max_length=100, blank=True, null=True)
    difficulty = models.CharField(max_length=1, choices=[
        ('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')
    ])


class UserWord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    remembered = models.BooleanField(default=False)
    last_reviewed = models.DateTimeField(default=timezone.now)
    review_count = models.IntegerField(default=0)
