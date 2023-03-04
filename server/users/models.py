from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

from .managers import CustomUserManager


class RoleCategory(Enum):
    TECHNICAL = 'Технічна'
    NOT_TECHnICAL = 'Не технічна'
    OTHER = 'Інша'


class Role(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in RoleCategory])

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = None
    role = models.ForeignKey(Role, related_name='users', on_delete=models.PROTECT, null=True)
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

