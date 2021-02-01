from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.adverts.api import views as av

router = DefaultRouter()
router.register(r"adverts", av.AdvertViewSet)

urlpatterns = [
    
    path(
            "<str:category>/adverts/", 
            av.CategoryListAPIView.as_view(), 
            name="create-advert"),

    path("search/", av.general_search, name="search"),

    path(
            "user/<int:user_id>/shop/", 
            av. SellerShopAPIView.as_view(), 
            name="seller-shop"),
            
    path("", include(router.urls)),
    
]