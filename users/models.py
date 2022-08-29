from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from model_utils.models import TimeStampedModel


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)


class User(TimeStampedModel, AbstractUser):

    id = models.BigAutoField(
        primary_key=True
    )

    email = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        verbose_name='이메일'
    )

    password = models.TextField()

    objects = UserManager()

    class Meta:
        verbose_name = '사용자 목록'
        db_table = 'users'
