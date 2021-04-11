import pika
import json
from flask import current_app


class RabbitMQPublisherException(Exception):
    def __init__(self, message, *args, **kwargs):
        self.message = message


class RabbitMQPublisher:

    def __init__(self):
        self.exchange_name = current_app.config["RABBITMQ_EXCHANGE"]
        self.host = current_app.config["RABBITMQ_HOST"]
        self.rabbit_user = current_app.config["RABBITMQ_USER"]
        self.rabbit_password = current_app.config["RABBITMQ_PASSWORD"]

        credentials = pika.PlainCredentials(self.rabbit_user, self.rabbit_password)
        params = pika.ConnectionParameters(
            host=self.host,
            port=5672,
            credentials=credentials
        )

        try:
            self.connection = pika.BlockingConnection(params)
            self.channel = self.connection.channel()
            self.channel.exchange_declare(
                exchange=self.exchange_name, exchange_type='fanout', durable=True)
        except Exception:
            raise RabbitMQPublisherException("Connection Problem")

    def publish(self, message):
        try:
            self.channel.basic_publish(
                exchange=self.exchange_name,
                routing_key='',
                body=json.dumps(message),
                properties=pika.BasicProperties(
                    delivery_mode=2,  # make message persistent
                )
            )
        except Exception:
            raise RabbitMQPublisherException("Publishing Problem")
