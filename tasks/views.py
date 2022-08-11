from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from tasks import models, serializers, permissions


class TaskViewSet(viewsets.ModelViewSet):
    """Handle creating and updating tasks"""
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.ViewOrUpdateOwnTask, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)

    def perform_create(self, serializer):
        """Sets the user profile to the current user"""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
