from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from groups import models, serializers, permissions


class GroupViewSet(viewsets.ModelViewSet):
    """Handle creating and updating groups"""
    serializer_class = serializers.GroupSerializer
    queryset = models.Group.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.ViewOrUpdateOwnGroup, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)

    def perform_create(self, serializer):
        """Sets the user profile to the current user"""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id)
