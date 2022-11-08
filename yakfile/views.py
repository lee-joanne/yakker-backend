from django.db.models import Count
from rest_framework import generics
from .models import Yakfile
from yakker.permissions import AuthenticatedOrReadOnly
from .serializers import YakfileSerializer


class ListYakfile(generics.ListAPIView):
    """
    Class-based view to list all yakfiles.
    """
    queryset = Yakfile.objects.annotate(
        post_count=Count('author__post', distinct=True)
    ).order_by('-created_at')
    permission_classes = [AuthenticatedOrReadOnly]
    serializer_class = YakfileSerializer


class DetailYakfile(generics.RetrieveUpdateAPIView):
    """
    Class-based detailed view to retrieve or update a profile
    if you're the owner.
    """
    queryset = Yakfile.objects.annotate(
        post_count=Count('author__post', distinct=True)
    ).order_by('-created_at')
    permission_classes = [AuthenticatedOrReadOnly]
    permission_classes = [AuthenticatedOrReadOnly]
    serializer_class = YakfileSerializer
