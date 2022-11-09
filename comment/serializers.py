from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.ReadOnlyField(source='commenter.username')

    class Meta:
        model = Comment
        fields = [
            'id', 'commenter', 'created_at', 'updated_at', 'post',
            'content',
        ]
