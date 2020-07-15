from rest_framework import generics, viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import  MultiPartParser, FormParser, FileUploadParser

from adverts.api.permissions import *
from users.models import CustomUser

from adverts.api.serializers import *
from core.utils import generate_random_string

class SearchList(generics.ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    filter_backend = [filters.SearchFilter]
    search_fields = ["name"]

class AdvertViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Advert.objects.all().order_by("-date_created")
    lookup_field = 'slug'
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    parser_classes = [MultiPartParser, FormParser]

    def perform_update(self, serializer):
        cat = self.request.data["category"] 
        category = get_object_or_404(Category, name=cat)
        serializer.save(category=category)

    def perform_create(self, serializer):
        slug = self.request.data["name"] + generate_random_string()
        cat = self.request.data["category"] 
        user = self.request.user
        category = get_object_or_404(Category, name=cat)

        serializer.save(slug=slug, user=user, category=category)

    
class CategoryListAPIView(generics.ListAPIView):
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("category")
        return Advert.objects.filter(category__name=kwarg_slug).order_by("-date_created")

class SellerShopAPIView(generics.ListAPIView):
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        user = get_object_or_404(CustomUser, id=user_id)
        return user.adverts.all().order_by("-date_created")