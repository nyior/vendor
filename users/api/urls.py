from django.urls import path, include
from users.api.views import *
from rest_framework.routers import DefaultRouter

#profile image viewset


urlpatterns = [
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('users/<int:user_id>/review-create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('users/<int:user_id>/reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('users/currentUser/', CurrentUserView.as_view(), name='current-user'),
    path('users/<int:user_id>/adverts/', AdsListAPIView.as_view(), name='adverts-list'),
    path('reviews/<int:pk>/', ReviewRUDAPIView.as_view(), name ='review-detail'),
    path("avatar/", AvatarUpdateView.as_view(), name = 'avatar')
]