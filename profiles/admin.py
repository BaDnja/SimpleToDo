from django.contrib import admin
from profiles import models


@admin.register(models.UserProfile)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "is_staff")
    list_display_links = ("first_name",)
    list_per_page = 25
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("is_active", "is_staff", "is_superuser")
