from django.db import IntegrityError
from rest_framework import serializers
from .models import PostReyakks


class PostReyakksSerializer(serializers.ModelSerializer):
    post_reyakker = serializers.ReadOnlyField(source='liker.username')

    class Meta:
        model = PostReyakks
        fields = [
            'post_reyakker', 'created_at', 'post'
        ]

    def create(self, validated_data):
        """
        Integrity error check taken from Code Institute's DRF example project.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
