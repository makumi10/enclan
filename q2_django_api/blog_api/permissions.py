from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # everyone can read, only the author can edit/delete their own post
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
