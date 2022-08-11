from rest_framework import permissions


class ViewOrUpdateOwnTask(permissions.BasePermission):
    """Allow users to view and edit their own task"""

    def has_object_permission(self, request, view, obj):
        """Request user is trying to view or edit their own task"""
        return obj.user.id == request.user.id
