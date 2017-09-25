import injector
import tornado.httpserver
import tornado.ioloop
import tornado.web

from url_shortener.handlers.module import HandlersModule
from url_shortener.lib.configuration import Configuration


class App(object):
    def __init__(self, tornado_app):
        self.tornado_app = tornado_app

    def get_server(self):
        server = tornado.httpserver.HTTPServer(self.tornado_app)
        server.bind(8888)
        return server

    def add_handlers(self, app_handlers):
        self.tornado_app.add_handlers(r'.*', app_handlers)


class AppModule(injector.Module):
    def __init__(self, conf):
        self.conf = conf

    def configure(self, binder: injector.Binder):
        binder.install(HandlersModule)

    @injector.provider
    def configuration(self) -> Configuration:
        return self.conf

    @injector.provider
    def tornado_app(self) -> tornado.web.Application:
        return tornado.web.Application()

    @injector.inject
    @injector.provider
    def app(self, tornado_app: tornado.web.Application) -> App:
        return App(tornado_app)
