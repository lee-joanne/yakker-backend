from rest_framework import generics, permissions
from yakker.permissions import PostReyakkerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import PostReyakks
from .serializers import PostReyakksSerializer


class ListPostReyakks(generics.ListCreateAPIView):
    """
    Class-based view to list all post reyakks (likes).
    """
    queryset = PostReyakks.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostReyakksSerializer

    def perform_create(self, serializer):
        serializer.save(liker=self.request.user)


class DetailPostReyakks(generics.RetrieveDestroyAPIView):
    """
    Class-based detailed view to retrieve a reyakks.
    Can delete a comment if you're the liker.
    """
    queryset = PostReyakks.objects.all()
    permission_classes = [PostReyakkerOrReadOnly]
    serializer_class = PostReyakksSerializer
