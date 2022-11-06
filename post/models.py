from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Class-based model for Posts.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/',
        blank=True
    )
    content = models.TextField(blank=True)
    title = models.CharField(max_length=300)
    reyakks = models.ManyToManyField(User, related_name="reyakks", blank=True)

    class Meta:
        """
        Class Meta to set the order of the posts, newest first
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Function to create the string for representing yakfile model in admin
        """
        return f"{self.author}'s post called '{self.title}'"
