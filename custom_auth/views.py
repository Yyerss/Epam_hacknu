from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from .models import CustomUser
from django.utils import timezone
from .serializers import *
from rest_framework import generics
from rest_framework import mixins
from .authentication import EmailPhoneUsernameAuthenticationBackend as EoP
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.


class UserLoginView(generics.GenericAPIView):
    serializer_class = EmailLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = EoP.authenticate(request, username=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                'refresh': str(refresh),
                'access': access_token
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Неправильный логин или пароль'}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterUserView(generics.GenericAPIView, mixins.CreateModelMixin):
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        if CustomUser.objects.filter(email=request.data.get('email')).exists():
            return Response(
                {'error': 'Указанный адрес электронной почты уже зарегистрирован!'},
                status=status.HTTP_400_BAD_REQUEST)
        else:
            email = request.data.get('email')
            # send_mail('Account registration successful',
            #           'Your account has been registered successfully.',
            #           'abeubazekadilnegrila@gmail.com',
            #           [email],
            #           fail_silently=False
            #           )
            return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        return {'Location': str(data['id'])}


from django.shortcuts import render

# Create your views here.
