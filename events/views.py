import json
import logging

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Movie, CustomUser
from events.serializers import MovieTotalWatchTimeSerializer, UserTotalWatchTimeSerializer
from rabbitmq import rabbitmq_client


class EventAPI(APIView):

    def post(self, request):
        logging.info(msg=f"received data from request: {request.data}")
        rabbitmq_client.publish(json.dumps(request.data))

        return Response("ok", status=status.HTTP_200_OK)


class UserTotalWatchTimeAPI(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserTotalWatchTimeSerializer
    lookup_field = "username"


class MovieTotalWatchTimeAPI(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieTotalWatchTimeSerializer
