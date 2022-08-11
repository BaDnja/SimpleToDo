from rest_framework import serializers

from lists.models import List
from tasks.models import Task


class ListForeignKey(serializers.PrimaryKeyRelatedField):
    """Handle overriding get_queryset() and retrieving only current user lists"""
    def get_queryset(self):
        return List.objects.filter(user=self.context['request'].user)


class TaskSerializer(serializers.ModelSerializer):
    """Serialize a task object"""
    task_list = ListForeignKey(allow_null=True)

    class Meta:
        model = Task
        exclude = ("user",)
