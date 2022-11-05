from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Yakfile


class YakfileSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()

    def get_is_author(self, obj):
        request = self.context.get('request', None)
        return request.user == obj.author

    class Meta:
        model = Yakfile
        fields = [
            'id', 'author', 'created_at', 'image', 'content', 'is_author'
        ]