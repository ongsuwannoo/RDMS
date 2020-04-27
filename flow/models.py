from django.db import models

# Create your models here.

class Flow(models.Model):
    time_start = models.TimeField()
    time_end = models.TimeField()
    activity = models.CharField(max_length=255)
    sub_time = models.TimeField()
    desc = models.CharField(max_length=255)
    camp = models.ForeignKey(to='camp.Camp', on_delete=models.CASCADE)
    department = models.ForeignKey(to='camp.Department', on_delete=models.CASCADE, null=True)
    mc = models.ForeignKey(to='camp.MC', on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(to='locations.Location', on_delete=models.CASCADE)
    note = models.CharField(max_length=255, null=True)
