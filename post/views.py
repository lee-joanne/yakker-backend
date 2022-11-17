from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from yakker.permissions import AuthorOrReadOnly
from .serializers import PostSerializer


class ListPost(generics.ListCreateAPIView):
    """
    Class-based view to list all posts.
    """
    queryset = Post.objects.annotate(
        reyakks_count=Count('post_reyakker', distinct=True),
        comment_count=Count('comment', distinct=True),
    ).order_by('-created_at')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # user feed
        'author__followed_user__author__yakfile',
        # user liked posts
        'post_reyakker__post_reyakker__yakfile',
        # user posts
        'author__yakfile',
    ]
    search_fields = [
        'author__username',
        'title',
        'content',
    ]
    ordering_fields = [
        'reyakks_count',
        'comment_count',
        'post_reyakker__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    """
    Class-based detailed view to retrieve a post.
    Can edit, or delete a post if you're the author.
    """
    queryset = Post.objects.annotate(
        reyakks_count=Count('post_reyakker', distinct=True),
        comment_count=Count('comment', distinct=True),
    ).order_by('-created_at')
    permission_classes = [AuthorOrReadOnly]
    serializer_class = PostSerializer
