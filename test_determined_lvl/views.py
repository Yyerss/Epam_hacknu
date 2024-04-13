from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Question, TestSubmission, Answer
from rest_framework.permissions import IsAuthenticated
from .serializers import QuestionSerializer, TestSubmissionSerializer
from .services import calculate_language_level


class QuestionListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class TestSubmissionView(CreateAPIView):
    serializer_class = TestSubmissionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        submission, correct_count, total_count = serializer.save()
        return Response({
            'correct_answers': correct_count,
            'total_questions': total_count
        })
