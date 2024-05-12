import json
import logging

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Movie, CustomUser, WatchTime
from events.serializers import MovieTotalWatchTimeSerializer, UserTotalWatchTimeSerializer, \
    UserMovieTotalWatchTimeSerializer, EventSerializer
from rabbitmq import rabbitmq_client


class EventAPI(APIView):
    """
    📣 Event API: Receive data and publish to RabbitMQ

    This API endpoint receives data from the request and publishes it to RabbitMQ.

    **HTTP Method:** POST
    **Request Body:** JSON data
    **Response:** "ok" with HTTP 200 OK status
    """

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            logging.info(msg=f"received data from request: {request.data}")
            rabbitmq_client.publish(json.dumps(serializer.validated_data))
            return Response("ok", status=status.HTTP_200_OK)
        else:
            logging.error(msg=f"Invalid data received: {serializer.errors}")
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)


class UserTotalWatchTimeAPI(generics.RetrieveAPIView):
    """
    🕒️ User Total Watch Time API: Retrieve total watch time for a user

    This API endpoint retrieves the total watch time for a user.

    **HTTP Method:** GET
    **Path Parameter:** `username` (string)
    **Response:** JSON data with total watch time
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserTotalWatchTimeSerializer
    lookup_field = "username"


class MovieTotalWatchTimeAPI(generics.RetrieveAPIView):
    """
    🎥 Movie Total Watch Time API: Retrieve total watch time for a movie

    This API endpoint retrieves the total watch time for a movie.

    **HTTP Method:** GET
    **Path Parameter:** `pk` (integer)
    **Response:** JSON data with total watch time
    """
    queryset = Movie.objects.all()
    serializer_class = MovieTotalWatchTimeSerializer


class UserMovieWatchTimeAPI(generics.RetrieveAPIView):
    """
    👥 User Movie Watch Time API: Retrieve watch time for a user and movie

    This API endpoint retrieves the watch time for a user and a movie.

    **HTTP Method:** GET
    **Path Parameters:** `username` (string), `pk` (integer)
    **Response:** JSON data with watch time
    """
    queryset = WatchTime.objects.all()
    serializer_class = UserMovieTotalWatchTimeSerializer

    def get_object(self):
        username = self.kwargs['username']
        movie_pk = self.kwargs['movie_pk']
        queryset = self.queryset.filter(user__username=username, movie__id=movie_pk).first()
        return queryset
