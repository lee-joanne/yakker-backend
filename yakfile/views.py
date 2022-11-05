from rest_framework import generics
from .models import Yakfile
from .serializers import YakfileSerializer


class ListYakfile(generics.ListAPIView):
    """
    Class-based view to list all yakfiles.
    """
    queryset = Yakfile.objects.all().order_by('-created_at')
    serializer_class = YakfileSerializer


class DetailYakfile(generics.RetrieveUpdateAPIView):
    """
    Class-based detailed view to retrieve or update a profile if you're the owner.
    """
    queryset = Yakfile.objects.annotate().order_by('-created_at')
    serializer_class = YakfileSerializer
    

