from rest_framework import serializers
from .models import UserWord, Word
from django.utils import timezone


class RememberWordSerializer(serializers.ModelSerializer):
    word_id = serializers.PrimaryKeyRelatedField(source='word', queryset=Word.objects.all())

    class Meta:
        model = UserWord
        fields = ['word_id']

    def create(self, validated_data):
        user = self.context['request'].user
        word = validated_data['word']
        user_word, created = UserWord.objects.update_or_create(
            user=user,
            word=word,
            defaults={'remembered': True, 'last_reviewed': timezone.now(), 'review_count': 1}
        )
        return user_word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'kazakh', 'russian', 'english', 'difficulty']