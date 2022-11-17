from django.http import HttpResponse
from rest_framework import status


class ErrorCodeViewTestCase(APITestCase):
    def test_500_view(self, request):
        # Return an "Internal Server Error" 500 response code.
        return HttpResponse(status=500)
        self.assertEqual(500, response.status_code)
