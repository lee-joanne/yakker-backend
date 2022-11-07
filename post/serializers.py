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

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'created_at', 'updated_at', 'title',
            'image', 'content', 'is_author', 'yakfile_image'
        ]