from django.urls import path, include
from apps.users.api.views import *


urlpatterns = [
    path("user/wishlist/advert/<slug:slug>/", WishlistAPIView.as_view(), name="wishlist"),
    path("user/wishlist/", UserWishlistItemsAPIView.as_view(), name="wishlist-items"),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('users/<int:user_id>/review-create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('users/<int:user_id>/reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('users/currentUser/', CurrentUserView.as_view(), name='current-user'),
    path('users/<int:user_id>/adverts/', AdsListAPIView.as_view(), name='adverts-list'),
    path('reviews/<int:pk>/', ReviewRUDAPIView.as_view(), name ='review-detail'),
    path("avatar/", AvatarUpdateView.as_view(), name = 'avatar'),
]