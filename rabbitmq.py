import json


import pika

from events.models import WatchTime


class RabbitMQClient:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost')
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name, durable=False)

    def publish(self, message):
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_name,
                                   body=str(message))
        print(f"Published message to {self.queue_name}: {message}")

    def consume(self):
        def callback(ch, method, properties, body):
            print(f"Received message from {self.queue_name}: {body}")

        self.channel.basic_consume(queue=self.queue_name,
                                   on_message_callback=callback,
                                   auto_ack=True)
        print(f"Starting consumer for {self.queue_name}...")
        self.channel.start_consuming()

    def consume_and_save(self):
        def callback(ch, method, properties, body):
            decoded_body = body.decode('utf-8')
            data = json.loads(decoded_body)
            watch_time_saved: bool = WatchTime.save_watch_time_from_broker(data)

            if watch_time_saved:
                print('saved watch time')
            else:
                print("watch time has error")

        self.channel.basic_consume(queue=self.queue_name,
                                   on_message_callback=callback,
                                   auto_ack=True)
        print(f"Starting consumer for {self.queue_name}...")
        self.channel.start_consuming()

    def close(self):
        if self.connection.is_open:
            self.channel.stop_consuming()
            self.connection.close()
            print(f"Connection to {self.queue_name} closed.")


rabbitmq_client = RabbitMQClient(queue_name='watch-time')
