from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=70, null=False)

class Advert(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE, related_name="adverts")
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(null=True, blank=True)
    file = models.ImageField(upload_to="ads_pics", default="default.png", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="adverts")
    date_created = models.DateTimeField(auto_now_add=True)

    