import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.getenv('SECRET_KEY', "localkey")

    # Token expiration time in minutes
    ACCESS_TOKEN_DELTA = int(os.getenv('ACCESS_TOKEN_DELTA', 5))
    REFRESH_TOKEN_DELTA = int(os.getenv('REFRESH_TOKEN_DELTA', 2))

    FRONTEND_URL = "localhost:3000"

    RABBITMQ_EXCHANGE = os.getenv('RABBITMQ_EXCHANGE', 'test_exchange')
    RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')

    RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'guest')
    RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD', 'guest')


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False

    {{cookiecutter.project_name_uppercase}}_DB_ENGINE = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_ENGINE")
    {{cookiecutter.project_name_uppercase}}_DB_USER = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_USER")
    {{cookiecutter.project_name_uppercase}}_DB_PASSWORD = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_PASSWORD")
    {{cookiecutter.project_name_uppercase}}_DB_HOST = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_HOST")
    {{cookiecutter.project_name_uppercase}}_DB_PORT = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_PORT")
    {{cookiecutter.project_name_uppercase}}_DB_NAME = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_NAME")

    SQLALCHEMY_DATABASE_URI = (
        {% raw %}f'{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_ENGINE}://{% raw %}{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_USER}:'
        {% raw %}f'{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_PASSWORD}@{% raw %}{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_HOST}:'
        {% raw %}f'{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_PORT}/{% raw %}{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_NAME}'
    )

    EMAIL_USE_TLS = True
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_PORT = 587
    EMAIL_HOST_USER = "test_user"
    EMAIL_HOST_PASSWORD = r""
    EMAIL_SENDER_ADDRESS = "test_sender_address"
    FRONTEND_URL = "https://test.test.com"


class DevelopConfig(BaseConfig):
    DEBUG = True
    TESTING = False

    {{cookiecutter.project_name_uppercase}}_DB_ENGINE = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_ENGINE")
    {{cookiecutter.project_name_uppercase}}_DB_USER = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_USER")
    {{cookiecutter.project_name_uppercase}}_DB_PASSWORD = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_PASSWORD")
    {{cookiecutter.project_name_uppercase}}_DB_HOST = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_HOST")
    {{cookiecutter.project_name_uppercase}}_DB_PORT = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_PORT")
    {{cookiecutter.project_name_uppercase}}_DB_NAME = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_NAME")

    SQLALCHEMY_DATABASE_URI = (
        {% raw %}f'{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_ENGINE}://{% raw %}{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_USER}:'
        {% raw %}f'{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_PASSWORD}@{% raw %}{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_HOST}:'
        {% raw %}f'{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_PORT}/{% raw %}{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_NAME}'
    )

    EMAIL_USE_TLS = True
    EMAIL_HOST = "smtp.yoursmpt.com"
    EMAIL_PORT = 587
    EMAIL_HOST_USER = "test_user"
    EMAIL_HOST_PASSWORD = r""
    EMAIL_SENDER_ADDRESS = "test_sender_address"
    FRONTEND_URL = "https://test.test.com"


class LocalConfig(BaseConfig):
    DEBUG = True
    TESTING = False

    {{cookiecutter.project_name_uppercase}}_DB_ENGINE = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_ENGINE")
    {{cookiecutter.project_name_uppercase}}_DB_USER = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_USER")
    {{cookiecutter.project_name_uppercase}}_DB_PASSWORD = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_PASSWORD")
    {{cookiecutter.project_name_uppercase}}_DB_HOST = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_HOST")
    {{cookiecutter.project_name_uppercase}}_DB_PORT = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_PORT")
    {{cookiecutter.project_name_uppercase}}_DB_NAME = os.getenv("{{cookiecutter.project_name_uppercase}}_DB_NAME")

    SQLALCHEMY_DATABASE_URI = (
        {% raw %}f'{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_ENGINE}://{% raw %}{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_USER}:'
        {% raw %}f'{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_PASSWORD}@{% raw %}{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_HOST}:'
        {% raw %}f'{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_PORT}/{% raw %}{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_NAME}'
    )

    EMAIL_SENDER_ADDRESS = "noreply@test.com"
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_USE_TLS = False


class TestConfig(BaseConfig):
    DEBUG = False
    TESTING = True

    {{cookiecutter.project_name_uppercase}}_DB_ENGINE = os.getenv("TEST_DB_ENGINE", "postgresql")
    {{cookiecutter.project_name_uppercase}}_DB_USER = os.getenv("TEST_DB_USER", "postgres")
    {{cookiecutter.project_name_uppercase}}_DB_PASSWORD = os.getenv("TEST_DB_PASSWORD", "admin")
    {{cookiecutter.project_name_uppercase}}_DB_HOST = os.getenv("TEST_DB_HOST", "localhost")
    {{cookiecutter.project_name_uppercase}}_DB_PORT = os.getenv("TEST_DB_PORT", "5432")
    {{cookiecutter.project_name_uppercase}}_DB_NAME = os.getenv("TEST_DB_NAME", "test_db")

    RABBITMQ_USER = os.getenv('TEST_RABBITMQ_USER', 'test')
    RABBITMQ_PASSWORD = os.getenv('TEST_RABBITMQ_PASSWORD', 'test')

    SQLALCHEMY_DATABASE_URI = (
        {% raw %}f'{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_ENGINE}://{% raw %}{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_USER}:'
        {% raw %}f'{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_PASSWORD}@{% raw %}{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_HOST}:'
        {% raw %}f'{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_PORT}/{% raw %}{{% endraw %}{{cookiecutter.project_name_uppercase}}_DB_NAME}'
    )

    EMAIL_SENDER_ADDRESS = "noreply@digeiz.com"
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_USE_TLS = False
