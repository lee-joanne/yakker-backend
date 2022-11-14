from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from .models import Post
from yakker.permissions import AuthorOrReadOnly
from .serializers import PostSerializer


class ListPost(generics.ListCreateAPIView):
    """
    Class-based view to list all posts.
    """
    queryset = Post.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    """
    Class-based detailed view to retrieve a post.
    Can edit, or delete a post if you're the author.
    """
    queryset = Post.objects.all()
    permission_classes = [AuthorOrReadOnly]
    serializer_class = PostSerializer
