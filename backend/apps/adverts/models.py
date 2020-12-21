from django.db import models
from django.conf import settings


class Category(models.Model):

    """ This class models an advert category. 
        E.g. : video game, fashion etc.
    """

    name = models.CharField(max_length=70, null=False)

class Advert(models.Model):

    """ This class models an advert object. 
    """
    
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

    