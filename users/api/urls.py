from django.urls import path, include
from users.api.views import *

urlpatterns = [
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('users/<int:user_id>/review-create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('users/<int:user_id>/reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewRUDAPIView.as_view(), name ='review-detail'),
]