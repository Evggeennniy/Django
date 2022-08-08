from trainingapps.utils import logging_response, response_without_logging


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.path.startswith("/admin/") or request.path.startswith("/__debug__"):
            response = response_without_logging(self, request)

            return response

        else:
            response = logging_response(self, request)

            return response

        # Code to be executed for each request/response after
        # the view is called.
