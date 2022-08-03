from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.TextChoices):
    TODO = "todo", _("To do")
    IN_PROGRESS = "in_progress", _("In progress")
    ON_HOLD = "on_hold", _("On hold")
    DONE = "done", _("Done")


class Priority(models.TextChoices):
    LOW_PRIORITY = "low", _("Low priority")
    MEDIUM_PRIORITY = "medium", _("Medium priority")
    HIGH_PRIORITY = "high", _("High priority")
