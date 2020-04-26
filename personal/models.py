from django.db import models
from django.conf import settings

# Create your models here.
class Personal(models.Model):
    SEX = (
        ('M', 'MALE'),
        ('F', 'FEMALE')
    )
    
    sid = models.CharField(max_length=8, null=True)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=255)
    
    sex = models.CharField(choices=SEX, max_length=1)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=255, null=True)

    blood_type = models.CharField(max_length=2, null=True)
    birthday = models.DateField(null=True)
    religion = models.CharField(max_length=255, null=True)
    food_allergy = models.CharField(max_length=255, default='-')
    congenital_disease = models.CharField(max_length=255, default='-')
    shirt_size = models.CharField(max_length=5)
    
    profile_pic = models.ImageField(upload_to='profiles/')
