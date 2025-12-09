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
    

class RestrictAccessByTimeMiddleware:
    """
    Middleware that restricts access by returning an error 403 Forbidden
    if a user accesses the chat outside 9PM and 6PM.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        if current_hour < 9 or current_hour > 18:
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("Access to the chat is restricted to between 9AM and 6PM.")

        response = self.get_response(request)
        return response