from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def handler500(request):
    payload = {
        "message": "sorry, there appears to be an error... please try again.",
        "success": False,
        "data": None
    }
    return Response(data=payload, status=500, exception=True)