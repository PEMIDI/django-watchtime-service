from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from events.models import Movie, CustomUser


class UserTotalWatchTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'total_watch_time']


class MovieTotalWatchTimeSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'slug', 'total_watch_time']
