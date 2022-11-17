from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post
from post_reyakks.models import PostReyakks


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    yakfile_image = serializers.ReadOnlyField(
        source='author.yakfile.image.url')
    post_reyakks_id = serializers.SerializerMethodField()
    reyakks_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()

    def get_is_author(self, obj):
        request = self.context.get('request', None)
        return request.user == obj.author

    def validate_image(self, value):

        MEGABYTE_LIMIT = 1
        REQUIRED_WIDTH = 2500
        REQUIRED_HEIGHT = 2500

        if value.size > 1024 * 1024 * MEGABYTE_LIMIT:
            raise serializers.ValidationError(
                f'Sorry! The image width is larger than {MEGABYTE_LIMIT} mb!'
            )
        if value.image.width > REQUIRED_WIDTH:
            raise serializers.ValidationError(
                f'Sorry! The image width is larger than {REQUIRED_WIDTH} px!'
            )
        if value.image.height > REQUIRED_HEIGHT:
            raise serializers.ValidationError(
                f'Sorry! The image height is larger than {REQUIRED_HEIGHT} px!'
            )
        return value

    def get_post_reyakks_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            post_reyakks = PostReyakks.objects.filter(
                post_reyakker=user, post=obj
            ).first()
            return post_reyakks.id if post_reyakks else None
        return None

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'created_at',
            'updated_at',
            'title',
            'image',
            'content',
            'is_author',
            'yakfile_image',
            'post_reyakks_id',
            'reyakks_count',
            'comment_count',
        ]
