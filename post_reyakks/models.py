from django.db import models
from django.contrib.auth.models import User
from post.models import Post


class PostReyakks(models.Model):
    post_reyakker = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_reyakker', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['post_reyakker', 'post']

    def __str__(self):
        return f'{self.post_reyakker} liked {self.post}'