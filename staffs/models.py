from django.db import models
from personal.models import Personal

# Create your models here.

class Staff(models.Model):
    camp = models.ForeignKey(to='camp.Camp', on_delete=models.CASCADE)
    personal = models.OneToOneField(Personal, on_delete=models.CASCADE)
    department = models.ForeignKey(to='camp.Department', on_delete=models.CASCADE, null=True, blank=True)
    mc = models.ForeignKey(to='camp.MC', on_delete=models.CASCADE, null=True, blank=True)
    position = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    postscript = models.CharField(max_length=255, null=True)