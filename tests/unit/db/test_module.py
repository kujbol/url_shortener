from injector import with_injector
import pytest
from motor import MotorDatabase

from url_shortener.db.module import DBRepositoryModule


class TestDBRepositoryModule(object):
    @pytest.yield_fixture
    @with_injector(DBRepositoryModule)
    def db_repository_module(self):
        yield

    def test_db(self, db_repository_module, db: MotorDatabase):
        print(db)
