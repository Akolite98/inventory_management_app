from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    """Custom error handler for API responses."""
    response = exception_handler(exc, context)

    if response is not None:
        custom_response = {
            "status": response.status_code,
            "error": response.data,
            "message": "An error occurred, please check the details."
        }
        return Response(custom_response, status=response.status_code)

    return Response(
        {"status": status.HTTP_500_INTERNAL_SERVER_ERROR,
         "error": "Internal Server Error",
         "message": "Something went wrong on our side."},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
