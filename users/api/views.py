from rest_framework import generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.parsers import  MultiPartParser, FormParser, FileUploadParser

from users.api.serializers import *
from adverts.api.serializers import AdvertSerializer

from users.models import *
from adverts.models import Advert

from users.api.permissions import *

#user
class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [HasAccountOrReadOnly, IsAuthenticatedOrReadOnly]

class CurrentUserView(APIView):
    def get(self, request):
        user = request.user
        return Response({
            
            'username': user.username,

        })


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = AvatarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, HasAvatarOrReadOnly]

    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        user = self.request.user
        return user

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        reviewer = self.request.user
        user_id = self.kwargs.get("user_id")
        reviewee = get_object_or_404(CustomUser, pk=user_id)

        if reviewee.reviews.filter(reviewer=reviewer).exists():
            raise ValidationError("you have already reviewed this user")

        if reviewee == reviewer:
            raise ValidationError("you cannot review yourself")
        
        serializer.save(reviewer=reviewer, reviewee=reviewee)

class ReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Review.objects.filter(reviewee__id=user_id).order_by("-date_created")

class AdsListAPIView(generics.ListAPIView):
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Advert.objects.filter(user__id=user_id).order_by("-date_created")

class ReviewRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewerOrReadOnly, IsAuthenticatedOrReadOnly]
            

