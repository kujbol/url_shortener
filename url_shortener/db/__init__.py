# from motor.motor_tornado import MotorClient
# import injector
#
# from url_shortener.db.url_repository import UrlRepository
#
#
# class DBRepositoryModule(injector.Module):
#     @injector.inject
#     @injector.provider
#     def url_repository(self, db: MotorClient) -> UrlRepository:
#         return UrlRepository(db['urls'])
