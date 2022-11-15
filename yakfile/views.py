from django.db.models import Count
from rest_framework import generics, filters
from .models import Yakfile
from yakker.permissions import AuthorOrReadOnly
from .serializers import YakfileSerializer


class ListYakfile(generics.ListAPIView):
    """
    Class-based view to list all yakfiles.
    """
    queryset = Yakfile.objects.annotate(
        post_count=Count('author__post', distinct=True),
        follower_count=Count('author__followed_user', distinct=True),
        following_count=Count('author__author', distinct=True)
    ).order_by('-created_at')
    permission_classes = [AuthorOrReadOnly]
    serializer_class = YakfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'post_count',
        'follower_count',
        'following_count',
        'author__followed_user__created_at',
        'author__author__created_at',
    ]


class DetailYakfile(generics.RetrieveUpdateAPIView):
    """
    Class-based detailed view to retrieve or update a profile
    if you're the owner.
    """
    queryset = Yakfile.objects.annotate(
        post_count=Count('author__post', distinct=True),
        follower_count=Count('author__followed_user', distinct=True),
        following_count=Count('author__author', distinct=True)
    ).order_by('-created_at')
    permission_classes = [AuthorOrReadOnly]
    serializer_class = YakfileSerializer
