from django.contrib import admin

from tasks import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "due_date", "priority", "status", "user")
    list_display_links = ("name",)
    list_per_page = 25
    search_fields = ("name",)
    list_editable = ("due_date", "priority", "status")
    list_filter = ("status", "priority", "task_list", "task_list__group")
