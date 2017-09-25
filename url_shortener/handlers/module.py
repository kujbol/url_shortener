import injector

from url_shortener.db.module import DBRepositoryModule
from url_shortener.db.url_repository import UrlRepository
from url_shortener.handlers.short_url import ShortenedUrlHandler


class AppHandlers(list):
    pass


class HandlersModule(injector.Module):
    def configure(self, binder: injector.Binder):
        binder.install(DBRepositoryModule)

    @injector.inject
    @injector.provider
    def handlers(self, url_repository: UrlRepository) -> AppHandlers:
        return AppHandlers([
            (
                r"/([a-z|0-9]+)", ShortenedUrlHandler,
                dict(url_repository=url_repository)
            ),
        ])
