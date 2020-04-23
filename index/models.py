from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField
from personal.models import Personal

class user(AbstractUser):
    SEX = (
        ('M', 'MALE'),
        ('F', 'FEMALE')
    )
    personal = models.OneToOneField(Personal, on_delete=models.CASCADE, null=True)
    sid = models.CharField(max_length=8)
    sex = models.CharField(choices=SEX, max_length=1)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profiles/')


