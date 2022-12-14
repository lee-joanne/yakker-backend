from django.db import IntegrityError
from rest_framework import serializers
from .models import CommentReyakks


class CommentReyakksSerializer(serializers.ModelSerializer):
    """
    Class for comment reyakks serializer.
    """
    comment_reyakker = serializers.ReadOnlyField(
        source='comment_reyakker.username')

    class Meta:
        model = CommentReyakks
        fields = [
            'id', 'comment_reyakker', 'created_at', 'comment',
        ]

    def create(self, validated_data):
        """
        Integrity error check taken from Code Institute's DRF example project.
        Ensures duplicate comment reyakks returns error message to user.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
