"""
    api/permissions.py
    __________________
    Custom permissions setting as of v.1.0.
"""
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """ IsAuthorOrReadOnly - Is author or read only? Custom permission settings. """

    def has_object_permission(self, request, view, obj):
        """ Read-only permissions are allowed for any request. """
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post.
        return obj.User == request.user
