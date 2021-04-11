import pytest

from unittest.mock import patch

from {{cookiecutter.project_name}}_api.rabbitmq_manager import RabbitMQPublisher, RabbitMQPublisherException


class TestRabbitMQPublisher:

    @patch('{{cookiecutter.project_name}}_api.rabbitmq_manager.pika.BlockingConnection')
    def test_rabbitmq_publisher_fail_connection(self, mocked_connection, app):
        mocked_connection.side_effect = ValueError("on connect collapsed")

        with app.app_context():
            with pytest.raises(RabbitMQPublisherException) as publisherror:
                RabbitMQPublisher()

        assert publisherror.value
        assert publisherror.value.message == 'Connection Problem'

    @patch('{{cookiecutter.project_name}}_api.rabbitmq_manager.pika.BlockingConnection')
    def test_rabbitmq_publisher_fail_publish(self, mocked_connection, app):
        mocked_connection.return_value.channel.return_value.basic_publish.side_effect = ValueError("collapsed")

        with app.app_context():
            with pytest.raises(RabbitMQPublisherException) as publisherror:
                rabbit = RabbitMQPublisher()
                rabbit.publish("I will collapse")

        assert publisherror.value
        assert publisherror.value.message == 'Publishing Problem'
