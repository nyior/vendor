from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import get_object_or_404

from adverts.api.permissions import *


from adverts.api.serializers import *
from core.utils import generate_random_string


class AdvertViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Advert.objects.all()
    lookup_field = 'slug'
    serializer_class = AdvertSerializer
    permission_classes = [IsUserOrReadOnly, IsAuthenticatedOrReadOnly]

class AdvertCreateAPIView(generics.CreateAPIView):
    queryset =  Advert.objects.all()
    serializer_class =  AdvertSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        slug = self.request.data["name"] + generate_random_string()
        user = self.request.user
        cat = self.kwargs.get('category')
        category = get_object_or_404(Category, name=cat)

        serializer.save(slug=slug, user=user, category=category)

class CategoryListAPIView(generics.ListAPIView):
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("category")
        return Advert.objects.filter(category__name=kwarg_slug).order_by("-date_created")