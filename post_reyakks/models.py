from django.db import models
from django.contrib.auth.models import User
from post.models import Post


class PostReyakks(models.Model):
    """
    Class-based model for Posts Reyakks.
    """
    post_reyakker = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        related_name='post_reyakker',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Class Meta to set the order of the posts reyakks, newest first.
        """
        ordering = ['-created_at']
        unique_together = ['post_reyakker', 'post']

    def __str__(self):
        """
        Function to create the string for representing Post Reyakks model
        in admin.
        """
        return f'{self.post_reyakker} liked {self.post}'
