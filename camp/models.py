from django.db import models
from index.views import user

# Create your models here.
class Camp(models.Model):
    head = models.ForeignKey(user, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    logo = models.ImageField(upload_to='logo/')

class Department(models.Model):
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    typeOfDepartment = models.CharField(max_length=255)
    desc = models.TextField()

class MC(models.Model):
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    typeOfMC = models.CharField(max_length=255)
    desc = models.TextField()
