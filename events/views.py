import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rabbitmq import rabbitmq_client


class EventAPI(APIView):

    def post(self, request):
        logging.info(msg=f"received data from request: {request.data}")
        rabbitmq_client.publish(request.data)

        return Response("ok", status=status.HTTP_200_OK)
