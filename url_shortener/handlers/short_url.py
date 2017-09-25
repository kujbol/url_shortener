import tornado.web


class ShortenedUrlHandler(tornado.web.RequestHandler):
    def initialize(self, url_repository):
        self.url_repository = url_repository

    def get(self, url_id):
        redirection_url = self.url_repository.get_url_redirection(url_id)
        if redirection_url:
            self.redirect(redirection_url)
        self.send_error(404)
