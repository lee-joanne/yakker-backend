from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    reyakks_count = serializers.SerializerMethodField()

    def get_is_author(self, obj):
        request = self.context.get('request', None)
        return request.user == obj.author

    def get_reyakks_count(self, obj):
        return obj.reyakks.count()

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'created_at', 'updated_at', 'title',
            'image', 'content', 'is_author', 'reyakks', 'reyakks_count'
        ]