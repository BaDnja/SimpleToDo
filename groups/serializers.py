from rest_framework import serializers
from groups import models


class GroupSerializer(serializers.ModelSerializer):
    """Serialize a group object"""

    class Meta:
        model = models.Group
        fields = '__all__'
