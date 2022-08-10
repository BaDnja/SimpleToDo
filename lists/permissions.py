from rest_framework import permissions


class ViewOrUpdateOwnList(permissions.BasePermission):
    """Allow users to view and edit their own list"""

    def has_object_permission(self, request, view, obj):
        """Request user is trying to view or edit their own list"""
        return obj.user.id == request.user.id
