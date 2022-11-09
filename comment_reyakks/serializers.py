from rest_framework import serializers
from .models import CommentReyakks


class CommentReyakksSerializer(serializers.ModelSerializer):
    comment_reyakker = serializers.ReadOnlyField(source='comment_reyakker.username')

    class Meta:
        model = CommentReyakks
        fields = [
            'comment_reyakker', 'created_at', 'comment'
        ]
