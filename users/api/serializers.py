from rest_framework import serializers

from datetime import datetime, timezone
from django.utils.timesince import timesince

from users.models import CustomUser, Review

class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    profile_picture = serializers.ImageField(required=False)
    reviews = serializers.SerializerMethodField()
    current_user_has_reviewed = serializers.SerializerMethodField()

    
    class Meta:
        model = CustomUser
        fields = ['current_user_has_reviewed','id', 'username', 'email', 'reviews', 'profile_picture', 'phone_number', 'residence_hall', 'bio']

    def get_reviews(self, object):
        return object.reviews.count()

    def get_current_user_has_reviewed(self, instance):

        request = self.context.get("request")

        if request.user == instance:
            return True
            
        return instance.reviews.filter(reviewer__id=request.user.id).exists()


class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    reviewer = serializers.StringRelatedField(read_only=True)
    duration = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        exclude = ['reviewee', 'date_created']

    def get_duration(self, object):
        date_created = object.date_created
        now = datetime.now(timezone.utc)
        time_delta = timesince(date_created, now)
        return time_delta

    


    