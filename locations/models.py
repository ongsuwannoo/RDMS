from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    logo = models.ImageField(upload_to='logo/')
