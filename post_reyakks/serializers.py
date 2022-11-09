from rest_framework import serializers
from .models import PostReyakks


class PostReyakksSerializer(serializers.ModelSerializer):
    post_reyakker = serializers.ReadOnlyField(source='liker.username')

    class Meta:
        model = PostReyakks
        fields = [
            'post_reyakker', 'created_at', 'post'
        ]
