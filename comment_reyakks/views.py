from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from yakker.permissions import CommentReyakkerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import CommentReyakks, Comment
from .serializers import CommentReyakksSerializer


class ListCommentReyakks(generics.ListCreateAPIView):
    """
    Class-based view to list all post reyakks (likes).
    """
    queryset = CommentReyakks.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentReyakksSerializer

    def perform_create(self, serializer):
        comment = get_object_or_404(
            Comment, pk=serializer.initial_data['comment'])
        if comment.commenter == self.request.user:
            raise PermissionDenied
        else:
            serializer.save(comment_reyakker=self.request.user)


class DetailCommentReyakks(generics.RetrieveDestroyAPIView):
    """
    Class-based detailed view to retrieve a reyakks.
    Can delete a comment if you're the liker.
    """
    queryset = CommentReyakks.objects.all()
    permission_classes = [CommentReyakkerOrReadOnly]
    serializer_class = CommentReyakksSerializer
