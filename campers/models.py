from django.db import models
from personal.models import Personal
from camp.models import Camp

# Create your models here.
class Camper(models.Model):
    camp = models.OneToOneField(Camp, on_delete=models.CASCADE)
    personal = models.OneToOneField(Personal, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    parent_phone = models.CharField(max_length=10)
    parent_name = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='camperPic/')
    group = models.CharField(max_length=255, null=True)
    