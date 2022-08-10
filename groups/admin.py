from django.contrib import admin
from groups import models


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "modified_at", "user")
    list_display_links = ("name",)
    list_per_page = 25
    search_fields = ("name",)
