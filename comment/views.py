from rest_framework import generics, permissions
from yakker.permissions import AuthenticatedOrReadOnlyComments
from .models import Comment
from .serializers import CommentSerializer


class ListComment(generics.ListCreateAPIView):
    """
    Class-based view to list all comments.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(commenter=self.request.user)


class DetailComment(generics.RetrieveUpdateDestroyAPIView):
    """
    Class-based detailed view to retrieve a comment.
    Can edit, or delete a comment if you're the author.
    """
    queryset = Comment.objects.all()
    permission_classes = [AuthenticatedOrReadOnlyComments]
    serializer_class = CommentSerializer
