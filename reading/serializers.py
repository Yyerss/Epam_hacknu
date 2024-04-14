from rest_framework import serializers
from .models import ReadingR, QuestionR, AnswerR

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerR
        fields = ['id', 'text']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = QuestionR
        fields = ['id', 'prompt', 'answers']

class ReadingSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = ReadingR
        fields = ['id', 'content', 'questions']