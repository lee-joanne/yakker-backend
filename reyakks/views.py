from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Reyakks
from .serializers import ReyakksSerializer


class ListReyakks(generics.ListCreateAPIView):
    """
    Class-based view to list all comments.
    """
    queryset = Reyakks.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReyakksSerializer

    def perform_create(self, serializer):
        serializer.save(liker=self.request.user)


class DetailReyakks(generics.RetrieveDestroyAPIView):
    """
    Class-based detailed view to retrieve a comment.
    Can edit, or delete a comment if you're the author.
    """
    queryset = Reyakks.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReyakksSerializer
