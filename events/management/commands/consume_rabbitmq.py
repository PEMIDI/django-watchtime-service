from django.core.management.base import BaseCommand
from rabbitmq import rabbitmq_client


class Command(BaseCommand):
    help = 'Consume RabbitMQ messages and save to database'

    def handle(self, *args, **options):
        rabbitmq_client.consume_and_save()
        self.stdout.write('Consuming RabbitMQ messages and saving to database...')
