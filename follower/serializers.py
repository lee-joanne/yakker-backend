from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    followed_username = serializers.ReadOnlyField(source='followed_user.username')
    is_author = serializers.SerializerMethodField()

    def get_is_author(self, obj):
        request = self.context.get('request', None)
        return request.user == obj.author

    class Meta:
        model = Follower
        fields = [
            'id', 'author', 'followed_user', 'created_at', 'followed_username', 'is_author',
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