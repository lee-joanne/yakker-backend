from rest_framework import serializers
from .models import Comment
from comment_reyakks.models import CommentReyakks


class CommentSerializer(serializers.ModelSerializer):
    """
    Class for Comment serializer.
    """
    commenter = serializers.ReadOnlyField(source='commenter.username')
    comment_reyakks_id = serializers.SerializerMethodField()
    comment_reyakks_count = serializers.ReadOnlyField()
    yakfile_id = serializers.ReadOnlyField(source="commenter.yakfile.id")
    yakfile_image = serializers.ReadOnlyField(
        source="commenter.yakfile.image.url"
    )

    def get_comment_reyakks_id(self, obj):
        """
        Serializer method field to get comment
        reyakks id number if user is authenticated.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            comment_reyakks = CommentReyakks.objects.filter(
                comment_reyakker=user, comment=obj
            ).first()
            return comment_reyakks.id if comment_reyakks else None
        return None

    class Meta:
        model = Comment
        fields = [
            'id', 'commenter', 'created_at', 'updated_at', 'post',
            'content', 'comment_reyakks_id', 'comment_reyakks_count',
            'yakfile_id', 'yakfile_image',
        ]
