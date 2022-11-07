from rest_framework.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    yakfile_image = serializers.ReadOnlyField(source='author.yakfile.image.url')

    def get_is_author(self, obj):
        request = self.context.get('request', None)
        return request.user == obj.author

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'created_at', 'updated_at', 'title',
            'image', 'content', 'is_author', 'yakfile_image'
        ]