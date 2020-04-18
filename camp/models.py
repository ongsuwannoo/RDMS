from django.db import models
from index.views import user

# Create your models here.
class Camp(models.Model):
    head = models.OneToOneField(user, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    logo = models.ImageField(upload_to='logo/')