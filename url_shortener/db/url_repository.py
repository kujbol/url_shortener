class UrlRepository(object):
    def __init__(self, async_collection):
        self.async_collection = async_collection

    async def get_url_redirection(self, url_id):
        url = await self.async_collection.find_one({'url_id': url_id})
        if url:
            return url.get('url_redirection')
