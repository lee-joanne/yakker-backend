from rest_framework import serializers
from .models import Yakfile


class YakfileSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')


    class Meta:
        model = Yakfile
        fields = [
            'id', 'author', 'created_at', 'image', 'content'
        ]
