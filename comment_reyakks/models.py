from django.db import models
from django.contrib.auth.models import User
from comment.models import Comment


class CommentReyakks(models.Model):
    comment_reyakker = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='comment_reyakker', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['comment_reyakker', 'comment']

    def __str__(self):
        return f'{self.comment_reyakker} liked {self.comment}'