"""
Module creates app-instance and client-instance
to simulate interaction "server-client"
"""

import pytest
from web.main_app import create_app


@pytest.fixture
def app():
    # create app instance for tests
    app = create_app({
        'TESTING': True,
    })
    yield app


@pytest.fixture
def client(app):
    # create client instance to simulate client's requests
    return app.test_client()
