from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from events.models import Movie, CustomUser, WatchTime


class EventSerializer(serializers.Serializer):
    """
    **Event Serializer**

    Validates incoming data for the Event API.


    **Validation:**

    This serializer validates the incoming data to ensure it conforms to the expected format.

    * **user**: Must be a string with a maximum length of 255 characters.
    * **slug**: Must be a string with a maximum length of 255 characters.
    * **at**: Must be an integer.

    **Example:**

    ```
    {
        "user": "2fvkqoxolhs81",
        "slug": "3er6ivu3j0e2f",
        "at": 407
    }
    ```
    """
    user = serializers.CharField(max_length=255)
    slug = serializers.CharField(max_length=255)
    at = serializers.IntegerField()


class UserTotalWatchTimeSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomUser model to retrieve total watch time 🕰️

    Attributes:
    - username (str): Username of the user
    - total_watch_time (int): Total watch time of the user in seconds
    """

    class Meta:
        model = CustomUser  # 👥
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
        model = Movie  # 🎬
        fields = ['title', 'slug', 'total_watch_time']


class UserMovieTotalWatchTimeSerializer(ModelSerializer):
    class Meta:
        model = WatchTime
        fields = ['get_total_watch_time_per_user_movie']
