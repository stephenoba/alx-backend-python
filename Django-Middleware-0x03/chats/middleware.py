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
    

class OffensiveLanguageMiddleware:
    """
    tracks number of chat messages sent by each ip address and 
    implement a time based limit i.e 5 messages per minutes such 
    that if a user exceeds the limit, it blocks further messaging 
    and returns and error.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.message_counts = {}

    def __call__(self, request):
        ip = self.get_client_ip(request)
        current_time = datetime.now()

        # Initialize or reset count if more than a minute has passed
        if ip not in self.message_counts or (current_time - self.message_counts[ip]['time']).seconds > 60:
            self.message_counts[ip] = {'count': 0, 'time': current_time}

        self.message_counts[ip]['count'] += 1

        if self.message_counts[ip]['count'] > 5:
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("Message limit exceeded. Please wait before sending more messages.")

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    

class RolepermissionMiddleware:
    """
    Middleware that checks if a user has the required role to access certain chat features.
    If not, it returns a 403 Forbidden response.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if not user.is_authenticated or user.role != 'admin':
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("You do not have permission to access this feature.")

        response = self.get_response(request)
        return response