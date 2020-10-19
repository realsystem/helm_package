import pytest

from backend import create_backend


@pytest.fixture
def app():
    app = create_backend()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()
