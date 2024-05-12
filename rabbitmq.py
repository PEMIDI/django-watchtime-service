import json
import logging

import pika

from events.models import WatchTime


class RabbitMQClient:
    """
    🐰 RabbitMQ Client: Handles publishing and consuming messages to/from RabbitMQ

    This class provides a way to interact with RabbitMQ, allowing you to publish messages to a queue and consume them.

    **Queue Name:** `watch-time` (default)
    """

    def __init__(self, queue_name):
        """
        Initialize the RabbitMQ client with a queue name.

        :param queue_name: The name of the queue to interact with.
        """
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost')
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name, durable=False)
        self.logger = logging.getLogger(__name__)

    def publish(self, message):
        """
        Publish a message to the RabbitMQ queue.

        :param message: The message to publish as a string.
        """
        try:
            self.channel.basic_publish(exchange='',
                                       routing_key=self.queue_name,
                                       body=str(message))
            self.logger.info(f"Published message to {self.queue_name}: {message}")
        except pika.exceptions.ConnectionClosed:
            self.logger.error(f"Error: Connection to RabbitMQ closed unexpectedly.")
        except pika.exceptions.ChannelClosed:
            self.logger.error(f"Error: Channel to RabbitMQ closed unexpectedly.")
        except Exception as e:
            self.logger.error(f"Error: Failed to publish message to RabbitMQ: {e}")

    def consume(self):
        """
        Consume messages from the RabbitMQ queue.

        This method starts a consumer that will receive messages from the queue and print them.
        """
        def callback(ch, method, properties, body):
            try:
                self.logger.info(f"Received message from {self.queue_name}: {body}")
            except Exception as e:
                self.logger.error(f"Error: Failed to process message from RabbitMQ: {e}")

        try:
            self.channel.basic_consume(queue=self.queue_name,
                                       on_message_callback=callback,
                                       auto_ack=True)
            self.logger.info(f"Starting consumer for {self.queue_name}...")
            self.channel.start_consuming()
        except pika.exceptions.ConnectionClosed:
            self.logger.error(f"Error: Connection to RabbitMQ closed unexpectedly.")
        except pika.exceptions.ChannelClosed:
            self.logger.error(f"Error: Channel to RabbitMQ closed unexpectedly.")
        except Exception as e:
            self.logger.error(f"Error: Failed to start consumer for RabbitMQ: {e}")

    def consume_and_save(self):

        def callback(ch, method, properties, body):
            try:
                decoded_body = body.decode('utf-8')
                data = json.loads(decoded_body)
                watch_time_saved: bool = WatchTime.save_watch_time_from_broker(data)

                if watch_time_saved:
                    self.logger.info('saved watch time')
                else:
                    self.logger.error("watch time has error")
                    self.channel.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
            except json.JSONDecodeError:
                self.logger.error(f"Error: Invalid JSON message received from RabbitMQ: {body}")
            except Exception as e:
                self.logger.error(f"Error: Failed to process message from RabbitMQ: {e}")

        try:
            self.channel.basic_consume(queue=self.queue_name,
                                       on_message_callback=callback,
                                       auto_ack=True)
            self.logger.info(f"Starting consumer for {self.queue_name}...")
            self.channel.start_consuming()
        except pika.exceptions.ConnectionClosed:
            self.logger.error(f"Error: Connection to RabbitMQ closed unexpectedly.")
        except pika.exceptions.ChannelClosed:
            self.logger.error(f"Error: Channel to RabbitMQ closed unexpectedly.")
        except Exception as e:
            self.logger.error(f"Error: Failed to start consumer for RabbitMQ: {e}")

    def close(self):
        """
        Close the connection to RabbitMQ.

        This method stops the consumer and closes the connection to RabbitMQ.
        """
        try:
            if self.connection.is_open:
                self.channel.stop_consuming()
                self.connection.close()
                self.logger.info(f"Connection to {self.queue_name} closed.")
        except pika.exceptions.ConnectionClosed:
            self.logger.error(f"Error: Connection to RabbitMQ closed unexpectedly.")
        except Exception as e:
            self.logger.error(f"Error: Failed to close connection to RabbitMQ: {e}")


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

rabbitmq_client = RabbitMQClient(queue_name='watch-time')