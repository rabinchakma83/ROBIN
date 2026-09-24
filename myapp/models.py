from django.db import models
from django.contrib.auth.models import AbstractUser

class student(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    roll = models.IntegerField()
    semester = models.CharField(max_length=255, null=True)
    cgpa = models.FloatField(null=True,blank=True)
    def __str__(self):
        return f"{self.name} - {self.department}"

class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=255)
    