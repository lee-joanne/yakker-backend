from django.db import IntegrityError
from rest_framework import serializers
from .models import PostReyakks


class PostReyakksSerializer(serializers.ModelSerializer):
    """
    Class for post reyakks serializer.
    """
    post_reyakker = serializers.ReadOnlyField(source='post_reyakker.username')

    class Meta:
        model = PostReyakks
        fields = [
            'id', 'post_reyakker', 'created_at', 'post'
        ]

    def create(self, validated_data):
        """
        Integrity error check taken from Code Institute's DRF example project.
        Ensures duplicate post reyakks returns error message to user.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
