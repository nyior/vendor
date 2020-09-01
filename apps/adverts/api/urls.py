from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.adverts.api import views as qv

router = DefaultRouter()
router.register(r"adverts", qv.AdvertViewSet)

urlpatterns = [
    
    path("<str:category>/adverts/", qv.CategoryListAPIView.as_view(), name="create-advert"),
    path("search/", qv. SearchList.as_view(), name="search"),
    path("user/<int:user_id>/shop/", qv. SellerShopAPIView.as_view(), name="seller-shop"),
    path("", include(router.urls)),
    
]