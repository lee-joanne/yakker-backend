# Code taken from Code Institute's DRF Example Project
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    yakfile_id = serializers.ReadOnlyField(source='yakfile.id')
    yakfile_image = serializers.ReadOnlyField(source='yakfile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'yakfile_id', 'yakfile_image'
        )
