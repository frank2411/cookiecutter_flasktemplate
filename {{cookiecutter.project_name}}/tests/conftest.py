import pytest

from {{cookiecutter.project_name}}_api.app import create_app
from {{cookiecutter.project_name}}_api.models import db as rawdb


@pytest.fixture
def app():
    app = create_app(testing=True)
    return app


@pytest.fixture
def client(app):
    yield app.test_client()


@pytest.fixture
def db(app):
    with app.app_context():
        rawdb.init_db()

        yield rawdb

        rawdb.session.close()
        rawdb.drop_db()
