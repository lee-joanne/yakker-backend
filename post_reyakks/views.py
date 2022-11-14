from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from yakker.permissions import PostReyakkerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import PostReyakks, Post
from .serializers import PostReyakksSerializer


class ListPostReyakks(generics.ListCreateAPIView):
    """
    Class-based view to list all post reyakks (likes).
    """
    queryset = PostReyakks.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostReyakksSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=serializer.initial_data['post'])
        if post.author == self.request.user:
            raise PermissionDenied
        else:
            serializer.save(post_reyakker=self.request.user)


class DetailPostReyakks(generics.RetrieveDestroyAPIView):
    """
    Class-based detailed view to retrieve a reyakks.
    Can delete a comment if you're the liker.
    """
    queryset = PostReyakks.objects.all()
    permission_classes = [PostReyakkerOrReadOnly]
    serializer_class = PostReyakksSerializer
