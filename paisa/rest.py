import logging
log = logging.getLogger(__name__)

from requests import Request, Session

class Rest(object):
    session = None
    request = None

    def __init__(self, **rkwargs):
        self.session = Session()
        self.request = Request(**rkwargs)
    
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.session.close()

    def send(self, **kwargs):
        # prepare the request
        prepared_request = self.session.prepare_request(self.request)
        # send the request
        response = self.session.send(prepared_request, **kwargs)
        # return the response
        return response
