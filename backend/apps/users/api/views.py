from rest_framework import generics, mixins, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.parsers import  MultiPartParser, FormParser, FileUploadParser

from apps.users.api.serializers import *
from apps.adverts.api.serializers import AdvertSerializer

from apps.users.models import CustomUser, Review
from apps.adverts.models import Advert

from apps.users.api.permissions import *

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class CreateUser(generics.CreateAPIView):
    """ signup view """
    serializer_class = UserSerializer


class LoginView(APIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        
        if user:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
    

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    """ This retrieves a single user from the database
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [HasAccountOrReadOnly, IsAuthenticatedOrReadOnly]


class CurrentUserView(APIView):

    """ This view returns the current user
    """
    def get(self, request):
        user = request.user
        
        return Response({
            'username': user.username,
            'authenticated': user.is_authenticated,
            'user_id': user.id if user.is_authenticated else None

        })


class AvatarUpdateView(generics.UpdateAPIView):

    """ This allows users to update their avatar
    """

    serializer_class = AvatarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, HasAvatarOrReadOnly]

    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        user = self.request.user
        return user


class ReviewCreateAPIView(generics.CreateAPIView):

    """ This allows users create reviews
    """

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

    """ This returns a list of reviews for a user
    """

    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Review.objects.filter(reviewee__id=user_id).order_by("-date_created")


class AdsListAPIView(generics.ListAPIView):

    """ This returns a list of ads created by a user
    """

    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Advert.objects.filter(user__id=user_id).order_by("-date_created")


class ReviewRUDAPIView(generics.RetrieveUpdateDestroyAPIView):

    """ This allows users to rud a review
    """

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewerOrReadOnly, IsAuthenticatedOrReadOnly]


class UserWishlistItemsAPIView(generics.ListAPIView):

    """ This returns all the items in a user's wishlist
    """
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return user.wishlist.all()


class WishlistAPIView(APIView):
    
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, slug):
        advert = get_object_or_404(Advert, slug=slug) 
        user = self.request.user 

        user.wishlist.remove(advert) 
        user.save()

        serializer_context = {"request":request}
        serializer = self.serializer_class(advert, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug):
        advert = get_object_or_404(Advert, slug=slug) 
        user = self.request.user 

        user.wishlist.add(advert) 
        user.save()

        serializer_context = {"request":request}
        serializer = self.serializer_class(advert, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

