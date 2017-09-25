import injector
from motor.motor_tornado import (
    MotorClient,
    MotorDatabase,
)

from url_shortener.db.url_repository import UrlRepository
from url_shortener.lib.configuration import Configuration


class DBRepositoryModule(injector.Module):
    @injector.inject
    @injector.provider
    def db(self, configuration: Configuration) -> MotorDatabase:
        mongo_conf = configuration.mongo
        client = MotorClient(mongo_conf['url'])
        return client[mongo_conf['db']]

    @injector.inject
    @injector.provider
    def url_repository(self, db: MotorDatabase) -> UrlRepository:
        return UrlRepository(db['urls'])
