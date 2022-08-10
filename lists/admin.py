from django.contrib import admin
from lists import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "modified_at", "user")
    list_display_links = ("name",)
    list_per_page = 25
    search_fields = ("name",)
