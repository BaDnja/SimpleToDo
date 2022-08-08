from rest_framework import permissions


class ViewOrUpdateOwnGroup(permissions.BasePermission):
    """Allow users to view and edit their own group"""

    def has_object_permission(self, request, view, obj):
        """Request user is trying to view or edit their own group"""
        return obj.user.id == request.user.id
