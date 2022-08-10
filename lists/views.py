from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from lists import models, serializers, permissions


class ListViewSet(viewsets.ModelViewSet):
    """Handle creating and updating lists"""
    serializer_class = serializers.ListSerializer
    queryset = models.List.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.ViewOrUpdateOwnList, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)

    def perform_create(self, serializer):
        """Sets the user profile to the current user"""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
