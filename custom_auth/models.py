from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator
import random
import string
from django.utils import timezone


# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, photo=None, password=None):
        if not email:
            raise ValueError('Пользователи должны иметь адрес электронной почты или номер телефона')
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, photo=photo)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, photo=None, password=None):
        user = self.create_user(first_name=first_name, last_name=last_name, email=email, photo=photo, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    password_validator = RegexValidator(
        regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,20}$',
        message="Пароль должен быть длиной от 8 до 20 символов, начинаться с буквы и содержать как минимум одну цифру."
    )

    first_name = models.CharField(max_length=30, null=True, blank=True, default='')
    last_name = models.CharField(max_length=30, null=True, blank=True, default='')
    email = models.EmailField(unique=True)  # Уникальный email для каждого пользователя
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    password = models.CharField(validators=[password_validator], max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_profiles',
        blank=True,
        help_text='The groups this user belongs to',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_profiles',
        blank=True,
        help_text='Specific permissions for this user',
        verbose_name='user permissions',
    )
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return self.email