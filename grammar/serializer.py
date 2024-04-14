from rest_framework import serializers
from .models import GrammarRule, WordG

class GrammarRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammarRule
        fields = '__all__'

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordG
        fields = '__all__'