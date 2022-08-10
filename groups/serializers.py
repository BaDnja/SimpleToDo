from rest_framework import serializers
from groups.models import Group


class GroupSerializer(serializers.ModelSerializer):
    """Serialize a group object"""

    class Meta:
        model = Group
        exclude = ("user",)
