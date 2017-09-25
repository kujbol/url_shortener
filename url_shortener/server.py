import injector
import tornado.ioloop

from url_shortener.lib.configuration import Configuration
from url_shortener.handlers.module import AppHandlers
from url_shortener.app import (
    AppModule,
    App
)


if __name__ == '__main__':
    conf = Configuration(
        mongo_conf={'url': 'mongodb://localhost', 'db': 'url_shortener'}
    )
    injection = injector.Injector(AppModule(conf))
    app = injection.get(App)
    server = app.get_server()
    server.start(0)

    # add handlers later to start connection after fork
    app.add_handlers(injection.get(AppHandlers))

    tornado.ioloop.IOLoop.current().start()
