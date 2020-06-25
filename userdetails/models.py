from django.db import models

# Create your models here

class details(models.Model):
    email = models.CharField(max_length=255)
    first_name=models.CharField(max_length=255, blank=True, null=True)
    last_name=models.CharField(max_length=255, blank=True, null=True)
    contact=models.IntegerField()
    gender=models.CharField(max_length=250, blank=True, null=True)
    citizen = models.BooleanField(default=False)
    water_dep = models.BooleanField(default=False)
    elec_dept = models.BooleanField(default=False)
    road_dept = models.BooleanField(default=False)

    def __str__(self):
        return self.email