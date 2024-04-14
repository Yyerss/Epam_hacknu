from django.db import models


# Create your models here.
class ReadingR(models.Model):
    content = models.TextField()


class QuestionR(models.Model):
    reading = models.ForeignKey(ReadingR, related_name='questions', on_delete=models.CASCADE)
    prompt = models.TextField()


class AnswerR(models.Model):
    question = models.ForeignKey(QuestionR, related_name='answers', on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
