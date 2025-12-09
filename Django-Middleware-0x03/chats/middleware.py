from datetime import datetime

class RequestLoggingMiddleware:
    """
    Middleware that logs each incoming request's method and path.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the request time, user and path
        print(f"{datetime.now()} - User: {request.user} - Path: {request.path}")

        response = self.get_response(request)
        return response