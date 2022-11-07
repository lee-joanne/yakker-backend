from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import serializers
from .models import Yakfile


class YakfileSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    author_age_days = serializers.SerializerMethodField()
    post_count = serializers.ReadOnlyField()

    def get_is_author(self, obj):
        request = self.context.get('request', None)
        return request.user == obj.author

    def get_author_age_days(self, obj):
        return (now() - obj.created_at).days


    class Meta:
        model = Yakfile
        fields = [
            'id', 'author', 'created_at', 'image', 'content', 'is_author', 'author_age_days', 'post_count'
        ]