from django.db import models
from django.contrib.auth.models import User
from comment.models import Comment


class CommentReyakks(models.Model):
    """
    Class-based model for Comment Reyakks.
    """
    comment_reyakker = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment,
        related_name='comment_reyakker',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Class Meta to set the order of the comments reyakks,
        newest first.
        """
        ordering = ['-created_at']
        unique_together = ['comment_reyakker', 'comment']

    def __str__(self):
        """
        Function to create the string for representing Comment Reyakks model
        in admin.
        """
        return f'{self.comment_reyakker} liked {self.comment}'
