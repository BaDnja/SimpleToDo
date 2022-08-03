from django.db import models
from django.utils.translation import gettext_lazy as _
from codebooks import models as codebooks_models


class AbstractBase(models.Model):
    """Abstract class for common objects like: tasks, lists, groups, etc."""
    name = models.CharField(_("name"), max_length=128)
    description = models.TextField(_("description"), max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("date and time when created"))
    modified_at = models.DateTimeField(auto_now=True, verbose_name=_("date and time when last modified"))

    class Meta:
        abstract = True


class Group(AbstractBase):
    """Class for grouping multiple lists."""

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")
