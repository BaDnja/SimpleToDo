from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from groups import models, serializers, permissions


class GroupViewSet(viewsets.ModelViewSet):
    """Handle creating and updating groups"""
    serializer_class = serializers.GroupSerializer
    queryset = models.Group.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.ViewOrUpdateOwnGroup,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
