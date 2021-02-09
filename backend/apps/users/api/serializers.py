from rest_framework import serializers

from datetime import datetime, timezone
from django.utils.timesince import timesince

from apps.users.models import CustomUser, Review

from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    """Serializer class for user in order to transfer user data."""
    id = serializers.IntegerField(read_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'password', 'phone_number', 'token')
        extra_kwargs = {'password': {'write_only': True}}

    def get_token(self, instance):
        token, _ = Token.objects.get_or_create(user=instance)
        token = f"{token}"
        return token
    
    def create(self, validated_data):
        """Method for creating new users from posted data"""
        user = CustomUser(
            username=validated_data['username'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number'],
        )
        
        #Hash and save password
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class AvatarSerializer(serializers.ModelSerializer):
    """This serializes a user's avatar"""

    class Meta:
        model = CustomUser
        fields = ("profile_picture",)


class CustomUserSerializer(serializers.ModelSerializer):
    """ This serialiazes a custom user"""

    id = serializers.IntegerField(read_only=True)
    reviews = serializers.SerializerMethodField()
    current_user_has_reviewed = serializers.SerializerMethodField()
    profile_picture = serializers.ImageField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['profile_picture', 'current_user_has_reviewed','id', 'username', 'email', 'reviews', 'phone_number', 'residence_hall', 'bio']

    def get_reviews(self, object):
        return object.reviews.count()

    def get_current_user_has_reviewed(self, instance):

        request = self.context.get("request")

        if request.user == instance:
            return True
            
        return instance.reviews.filter(reviewer__id=request.user.id).exists()
    

class ReviewSerializer(serializers.ModelSerializer):

    """ This serializes a user review
    """

    id = serializers.IntegerField(read_only=True)
    reviewer = serializers.StringRelatedField(read_only=True)
    duration = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        exclude = ['date_created']

    def get_duration(self, object):
        date_created = object.date_created
        now = datetime.now(timezone.utc)
        time_delta = timesince(date_created, now)
        return time_delta

    


    