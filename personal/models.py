from django.db import models
from django.conf import settings

# Create your models here.
class Personal(models.Model):
    nick_name = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=2)
    birthday = models.DateField()
    religion = models.CharField(max_length=255)
    food_allergy = models.CharField(max_length=255)
    congenital_disease = models.CharField(max_length=255)
    shirt_size = models.CharField(max_length=1)
