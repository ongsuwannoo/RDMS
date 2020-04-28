from django.db import models
from personal.models import Personal
from camp.models import Camp

# Create your models here.
class Camper(models.Model):
    camp = models.ForeignKey(to='camp.Camp', on_delete=models.CASCADE)
    personal = models.OneToOneField(Personal, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    parent_phone = models.CharField(max_length=10)
    parent_name = models.CharField(max_length=255)
    group = models.CharField(max_length=255, null=True)

class Observe(models.Model):
    camper = models.ForeignKey(Camper, on_delete=models.CASCADE)
    time = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
