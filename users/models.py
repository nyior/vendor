from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    residence_hall = models.CharField(max_length=12, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profile_pic", default="default.png") 
#user-review
class Review(models.Model):
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE, related_name="reviews_created")
    reviewee = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, 
                                    on_delete=models.SET_NULL,
                                    related_name="reviews")
    rating = models.PositiveIntegerField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
