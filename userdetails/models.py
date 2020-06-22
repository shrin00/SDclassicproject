from django.db import models

# Create your models here

class details(models.Model):
    email = models.CharField(max_length=255)
    first_name=models.CharField(max_length=255, blank=True, null=True)
    last_name=models.CharField(max_length=255, blank=True, null=True)
    contact=models.IntegerField()
    gender=models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.email