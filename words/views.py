from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .services import calculate_language_level
from .serializers import *
from rest_framework.generics import CreateAPIView, GenericAPIView
from random import randint
from django.utils import timezone

# Create your views here.


class RememberWordView(CreateAPIView):
    serializer_class = RememberWordSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user_word = serializer.save()
        calculate_language_level(self.request.user)

        return user_word


class RandomWordView(GenericAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get(self, request, *args, **kwargs):
        count = self.get_queryset().count()
        if count == 0:
            return Response({'error': 'No words available'}, status=404)
        random_index = randint(0, count - 1)
        word = self.get_queryset()[random_index]
        serializer = self.get_serializer(word)
        return Response(serializer.data)
