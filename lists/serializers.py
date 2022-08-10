from rest_framework import serializers

from lists.models import List
from groups.models import Group


class GroupForeignKey(serializers.PrimaryKeyRelatedField):
    """Handle overriding get_queryset() and retrieving only current user groups"""
    def get_queryset(self):
        return Group.objects.filter(user=self.context['request'].user)


class ListSerializer(serializers.ModelSerializer):
    """Serialize a list object"""
    group = GroupForeignKey(allow_null=True)

    class Meta:
        model = List
        fields = ("name", "description", "group", "created_at", "modified_at")
