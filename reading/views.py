from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import QuestionR, AnswerR
from .serializers import QuestionSerializer
from rest_framework.generics import RetrieveAPIView
from .models import ReadingR
from .serializers import ReadingSerializer



class ReadingAPIView(RetrieveAPIView):
    queryset = ReadingR.objects.all()
    serializer_class = ReadingSerializer


