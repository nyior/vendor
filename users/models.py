from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    profile_picture = models.ImageField(upload_to="profile_pic")
    phone_number = models.CharField(max_length=15)
    residence_hall = models.CharField(max_length=12)
    bio = models.TextField()

class Review(models.Model):
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE, related_name="reviews_created")
    reviewee = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, 
                                    on_delete=models.SET_NULL,
                                    related_name="reviews")
    rating = models.PositiveIntegerField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
