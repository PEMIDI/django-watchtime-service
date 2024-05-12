from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from events.models import Movie, CustomUser


class UserTotalWatchTimeSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomUser model to retrieve total watch time 🕰️

    Attributes:
    - username (str): Username of the user
    - total_watch_time (int): Total watch time of the user in seconds
    """

    class Meta:
        model = CustomUser # 👥
        fields = ['username', 'total_watch_time']


class MovieTotalWatchTimeSerializer(ModelSerializer):
    """
    Serializer for Movie model to retrieve total watch time 🎥

    Attributes:
    - title (str): Title of the movie
    - slug (str): Slug of the movie
    - total_watch_time (int): Total watch time of the movie in seconds
    """

    class Meta:
        model = Movie # 🎬
        fields = ['title', 'slug', 'total_watch_time']