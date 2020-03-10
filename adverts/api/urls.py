from django.urls import include, path
from rest_framework.routers import DefaultRouter

from adverts.api import views as qv

router = DefaultRouter()
router.register(r"adverts", qv.AdvertViewSet)
 
urlpatterns = [
    path("image/", qv.ImageCreateAPIView.as_view(), name="image"),
    path("<str:category>/adverts/", qv.CategoryListAPIView.as_view(), name="create-advert"),
    path("", include(router.urls)),
    
]