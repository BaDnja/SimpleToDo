from django.db import models
from django.utils.translation import gettext_lazy as _

from codebooks.models import Status, Priority
from groups.models import AbstractBase
from lists import models as lists_models


class AbstractTask(AbstractBase):
    status = models.CharField(_("status"), max_length=128, choices=Status.choices,
                              default=Status.IN_PROGRESS)

    class Meta:
        abstract = True


class Task(AbstractTask):
    """Class for storing and manipulating Tasks."""
    due_date = models.DateField(_("due date"), blank=True, null=True)
    task_list = models.ForeignKey(lists_models.List, on_delete=models.CASCADE, verbose_name=_("list"),
                                  blank=True, null=True, related_name="tasks")
    priority = models.CharField(_("priority"), max_length=128, choices=Priority.choices,
                                default=Priority.MEDIUM_PRIORITY)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")
