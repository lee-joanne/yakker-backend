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

    def get_is_author(self, obj):
        request = self.context.get('request', None)
        return request.user == obj.author

    def get_author_age_days(self, obj):
        return (now() - obj.created_at).days

    def get_following_id(self, obj):
        """
        Code on get_following_id taken from CI's DRF Example Project
        """
        user = self.context['request'].user
        if user.is_authenticated:
            followed_user = Follower.objects.filter(
                author=user, followed_user=obj.author
            ).first()
            print(followed_user)
            return followed_user.id if followed_user else None
        return None


    class Meta:
        model = Yakfile
        fields = [
            'id', 'author', 'created_at', 'image', 'content', 'is_author', 'author_age_days', 'post_count', 'following_id',
        ]