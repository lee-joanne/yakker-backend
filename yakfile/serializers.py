from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import serializers
from .models import Yakfile
from follower.models import Follower


class YakfileSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    author_age_days = serializers.SerializerMethodField()
    post_count = serializers.ReadOnlyField()
    following_id = serializers.SerializerMethodField()
    follower_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_author(self, obj):
        """
        Serializer method field to check if logged in
        user is the author.
        """
        request = self.context.get('request', None)
        return request.user == obj.author

    def get_author_age_days(self, obj):
        """
        Serializer method field to get the yakfile age in days.
        """
        return (now() - obj.created_at).days

    def get_following_id(self, obj):
        """
        Code on get_following_id taken from CI's DRF Example Project.
        Gets the following id of user following the yakfile
        if user is authenticated.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            followed_user = Follower.objects.filter(
                author=user, followed_user=obj.author
            ).first()
            return followed_user.id if followed_user else None
        return None

    class Meta:
        model = Yakfile
        fields = [
            'id',
            'author',
            'created_at',
            'image',
            'content',
            'is_author',
            'author_age_days',
            'post_count',
            'following_id',
            'follower_count',
            'following_count',
        ]
