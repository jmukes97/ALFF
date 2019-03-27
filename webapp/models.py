from django.db import models

# Create your models here.
class user(models.Model):
    email = models.CharField(max_length=30, primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.CharField(max_length=30)
