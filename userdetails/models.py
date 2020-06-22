from django.db import models

# Create your models here

class details(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    contact=models.IntegerField()
    gender=models.CharField(max_length=250, blank=True, null=True)

    def __init__(self):
        return name