from django.db import models


class GrammarRule(models.Model):
    rule_text = models.TextField(unique=True, null=False, blank=False)


class WordG(models.Model):
    kazakh_word = models.CharField(max_length=100, null=True, blank=True)
    english_translation = models.CharField(max_length=100, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True, null=True, blank=True)
