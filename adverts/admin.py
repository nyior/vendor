from django.contrib import admin
from adverts.models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
   model = Category
   list_display = ['id', 'name']


class AdvertAdmin(admin.ModelAdmin):
   model = Advert
   list_display = ['user', 'name', 'price', 'quantity']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Advert, AdvertAdmin)

