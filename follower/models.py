from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Class-based model for Follower.
    """
    author = models.ForeignKey(
        User,
        related_name="author",
        on_delete=models.CASCADE)
    followed_user = models.ForeignKey(
        User,
        related_name="followed_user",
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Class Meta to set the order of the posts, newest first
        """
        ordering = ['-created_at']
        unique_together = ['author', 'followed_user']

    def __str__(self):
        """
        Function to create the string for representing yakfile model in admin
        """
        return f"{self.author} is following {self.followed_user}"
