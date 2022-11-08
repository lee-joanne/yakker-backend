from django.db import models
from django.contrib.auth.models import User
from post.models import Post


class Comment(models.Model):
    """
    Class-based model for Comments.
    """
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)

    class Meta:
        """
        Class Meta to set the order of the comments, newest first
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Function to create the string for representing yakfile model in admin
        """
        return f"{self.commenter}'s comment on '{self.post}'"
