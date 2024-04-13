from rest_framework import serializers
from .models import *


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'answers']


class AnswerSubmissionSerializer(serializers.Serializer):
    question_id = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all(),
        source='question',
        write_only=True
    )
    answer_id = serializers.PrimaryKeyRelatedField(
        queryset=Answer.objects.all(),
        source='answer',
        write_only=True
    )


class TestSubmissionSerializer(serializers.ModelSerializer):
    answers = AnswerSubmissionSerializer(many=True, write_only=True)

    class Meta:
        model = TestSubmission
        fields = ['answers']

    def create(self, validated_data):
        user = self.context['request'].user
        answers_data = validated_data.pop('answers')
        submission = TestSubmission.objects.create(user=user)

        correct_count = 0
        total_count = len(answers_data)

        for answer_data in answers_data:
            answer = answer_data['answer']
            submission.answers.add(answer)
            if answer.is_correct:
                correct_count += 1

        submission.save()
        return submission, correct_count, total_count
