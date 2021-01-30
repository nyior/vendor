from rest_framework import serializers
from apps.adverts.models import *
from apps.users.api.serializers import CustomUserSerializer

from datetime import datetime, timezone
from django.utils.timesince import timesince

class AdvertSerializer(serializers.ModelSerializer):

    """ This serializes an advert object

    """

    slug = serializers.SlugField(read_only=True)
    quantity = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)
    user = CustomUserSerializer(read_only=True)
    category = serializers.SerializerMethodField()
    advert_in_current_user_wishlist= serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Advert
        exclude = ("date_created",)

    def get_duration(self, object):
        date_created = object.date_created
        now = datetime.now(timezone.utc)
        time_delta = timesince(date_created, now)
        return time_delta

    def get_category(self, object):
        return object.category.name

    def get_advert_in_current_user_wishlist(self, object):
        request = self.context.get("request")
        user  = request.user
        return object.users.filter(id=user.id).exists()
