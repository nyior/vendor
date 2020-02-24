from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError

from users.api.serializers import *
from users.models import *
from users.api.permissions import *


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [HasAccountOrReadOnly, IsAuthenticatedOrReadOnly]

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

class ReviewRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewerOrReadOnly]
            

