from rest_framework import serializers
from .models import Reyakks


class ReyakksSerializer(serializers.ModelSerializer):
    liker = serializers.ReadOnlyField(source='liker.username')

    class Meta:
        model = Reyakks
        fields = [
            'liker', 'created_at', 'post',
        ]
