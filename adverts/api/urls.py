from django.urls import include, path
from rest_framework.routers import DefaultRouter

from adverts.api import views as qv

router = DefaultRouter()
router.register(r"adverts", qv.AdvertViewSet)
 
urlpatterns = [
    path("<str:category>/adverts/create/", qv.AdvertCreateAPIView.as_view(), name="create-advert"),
    path("<str:category>/adverts/", qv.CategoryListAPIView.as_view(), name="create-advert"),
    path("", include(router.urls)),
    
]