from rest_framework import permissions
# Code inspired from Django REST Framework Tutorial:
# https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/


class AuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission created to allow users to edit their posts only.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class CommenterOrReadOnly(permissions.BasePermission):
    """
    Custom permission created to allow commenters to edit their comments only.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.commenter == request.user


class PostReyakkerOrReadOnly(permissions.BasePermission):
    """
    Custom permission created to allow only the reyakker to delete their reyakks on posts.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.post_reyakker == request.user


class CommentReyakkerOrReadOnly(permissions.BasePermission):
    """
    Custom permission created to allow only the reyakker to delete their reyakk on comments.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.comment_reyakker == request.user
