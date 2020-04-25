from django.db import models
from personal.models import Personal
from camp.views import Camp

# Create your models here.

class Staff(models.Model):
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE)
    personal = models.OneToOneField(Personal, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
