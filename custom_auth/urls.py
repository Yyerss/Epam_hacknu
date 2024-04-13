from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('register/', views.RegisterUserView.as_view(), name='user_register'),
    path('password-reset-request/', views.PasswordResetRequestAPIView.as_view(), name='password_reset_request'),
    path('password-reset-confirm/', views.PasswordResetCompleteAPIView.as_view(), name='password_reset_confirm'),
    path('user/profile/', views.UserProfileView.as_view(), name='user-profile'),
]