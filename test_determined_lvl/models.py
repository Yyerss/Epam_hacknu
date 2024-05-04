from django.db import models
from custom_auth.admin import CustomUser


# Create your models here.


class Question(models.Model):
    text = models.TextField()
    level = models.CharField(max_length=2, choices=[
        ('A1', 'Beginner'), ('A2', 'Elementary'),
        ('B1', 'Intermediate'), ('B2', 'Upper Intermediate'),
        ('C1', 'Advanced'), ('C2', 'Proficiency')
    ])


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField()

    def __str__(self):
        return self.text


class TestSubmission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer, related_name='submissions')
