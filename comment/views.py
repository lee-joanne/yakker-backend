from django.db.models import Count
from rest_framework import generics, permissions, filters
from yakker.permissions import CommenterOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from .serializers import CommentSerializer


class ListComment(generics.ListCreateAPIView):
    """
    Class-based view to list all comments.
    """
    queryset = Comment.objects.annotate(
        comment_reyakks_count=Count('comment_reyakker', distinct=True),
        ).order_by('-created_at')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        # retrieve all comments associated with given post
        'post'
    ]
    ordering_fields = [
        'comment_reyakks_count',
        'comment_reyakker__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(commenter=self.request.user)


class DetailComment(generics.RetrieveUpdateDestroyAPIView):
    """
    Class-based detailed view to retrieve a comment.
    Can edit, or delete a comment if you're the author.
    """
    queryset = Comment.objects.annotate(
        comment_reyakks_count=Count('comment_reyakker', distinct=True),
        ).order_by('-created_at')
    permission_classes = [CommenterOrReadOnly]
    serializer_class = CommentSerializer
