from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Yakfile(models.Model):
    """
    Class-based model for the yakfile (profile) of users.
    """
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default-image_b21ozy'
    )
    content = models.TextField(blank=True)

    class Meta:
        """
        Class Meta to set the order of the yakfiles, newest first
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Function to create the string for representing Yakfile model in admin
        """
        return f"{self.author}'s yakfile"


def create_yakfile(sender, instance, created, **kwargs):
    """
    Function to create a yakfile automatically when new user is created.
    Code taken from Code Institute's DRF API project.
    """
    if created:
        Yakfile.objects.create(author=instance)


post_save.connect(create_yakfile, sender=User)
