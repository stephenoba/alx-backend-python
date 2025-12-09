from datetime import datetime

class RequestLoggingMiddleware:
    """
    Middleware that logs each user’s requests to a file, including the timestamp, user and the request path.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        log_entry = f"{datetime.now().isoformat()} - User: {user} - Path: {request.path}\n"
        with open('requests.log', 'a') as log_file:
            log_file.write(log_entry)

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