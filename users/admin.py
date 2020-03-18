from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser, Review
# Register your models here.

class CustomUserAdmin(UserAdmin):
   model = CustomUser
   list_display = ['username', 'email', 'is_staff']


class ReviewAdmin(admin.ModelAdmin):
   model = Review
   list_display = ['reviewer', 'reviewee', 'date_created']

# class WishlistAdmin(admin.ModelAdmin):
#    model = Wishlist
#    list_display = ['user', 'advert']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Review, ReviewAdmin)
#admin.site.register(Wishlist, WishlistAdmin)


