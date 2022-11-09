from django.db import models
from django.contrib.auth.models import User
from post.models import Post


class Reyakks(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='reyakks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['liker', 'post']

    def __str__(self):
        return f'{self.liker} liked {self.post}'