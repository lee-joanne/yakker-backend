# Code on 404 and 500 exception handling heavily inspired by
# YouTube Channel Cryce Truly on Django Exception Handling.
# Check README.md documentation for full link.

from django.http import JsonResponse


def error_404(request, exception):
    """
    JSON response handler for 404 error codes.
    """
    message = ('This page does not exist! Sorry.')

    response = JsonResponse(data={
        'message': message,
        'status_code': 404
    })
    response.status_code = 404
    return response


def error_500(request):
    """
    JSON response handler for 500 error codes.
    """
    message = ("An error occurred... it's our fault.")
    response = JsonResponse(data={
        'message': message,
        'status_code': 500
    })
    response.status_code = 500
    return response
