import pytest
import mongomock

from url_shortener.server import make_app


@pytest.fixture()
def app():
    return make_app()
