from rest_framework import generics
from .models import Post
from yakker.permissions import AuthenticatedOrReadOnly
from .serializers import PostSerializer


class ListPost(generics.ListCreateAPIView):
    """
    Class-based view to list all yakfiles.
    """
    queryset = Post.objects.all().order_by('-created_at')
    permission_classes = [AuthenticatedOrReadOnly]
    serializer_class = PostSerializer


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    """
    Class-based detailed view to retrieve or update a profile
    if you're the owner.
    """
    queryset = Post.objects.all()
    permission_classes = [AuthenticatedOrReadOnly]
    serializer_class = PostSerializer
