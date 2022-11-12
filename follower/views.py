from rest_framework import generics, permissions
from .models import Follower
from yakker.permissions import AuthorOrReadOnly
from .serializers import FollowerSerializer


class ListFollower(generics.ListCreateAPIView):
    """
    Class-based view to list all posts.
    """
    queryset = Follower.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DetailFollower(generics.RetrieveDestroyAPIView):
    """
    Class-based detailed view to retrieve a post.
    Can edit, or delete a post if you're the author.
    """
    queryset = Follower.objects.all()
    permission_classes = [AuthorOrReadOnly]
    serializer_class = FollowerSerializer
