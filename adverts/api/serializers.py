from rest_framework import serializers
from adverts.models import *
from users.api.serializers import CustomUserSerializer

from datetime import datetime, timezone
from django.utils.timesince import timesince

class AdvertSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    user = CustomUserSerializer(read_only=True)
    category = serializers.SerializerMethodField()
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

