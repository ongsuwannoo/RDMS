from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField
from personal.models import Personal

class user(AbstractUser):
    personal = models.OneToOneField(Personal, on_delete=models.CASCADE, null=True)
