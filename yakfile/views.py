from rest_framework import generics
from .models import Yakfile


class ListYakfile(generics.ListAPIView):
    queryset = Yakfile.objects.all().order_by('-created_at')
    serializer_class = YakfileSerializer


class DetailYakfile(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    queryset = Yakfile.objects.annotate().order_by('-created_at')
    serializer_class = YakfileSerializer

