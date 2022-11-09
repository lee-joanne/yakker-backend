from rest_framework import generics, permissions
from yakker.permissions import CommentReyakkerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import CommentReyakks
from .serializers import CommentReyakksSerializer


class ListCommentReyakks(generics.ListCreateAPIView):
    """
    Class-based view to list all post reyakks (likes).
    """
    queryset = CommentReyakks.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentReyakksSerializer

    def perform_create(self, serializer):
        serializer.save(comment_reyakker=self.request.user)


class DetailCommentReyakks(generics.RetrieveDestroyAPIView):
    """
    Class-based detailed view to retrieve a reyakks.
    Can delete a comment if you're the liker.
    """
    queryset = CommentReyakks.objects.all()
    permission_classes = [CommentReyakkerOrReadOnly]
    serializer_class = CommentReyakksSerializer
