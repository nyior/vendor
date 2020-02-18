from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    profile_picture = models.ImageField()
    phone_number = models.CharField(max_length=15)
    residence_hall = models.CharField(max_length=12)
    bio = models.TextField()