from django.db import models
from django.utils.translation import gettext_lazy as _
from groups import models as groups_models


class List(groups_models.AbstractBase):
    """Class for grouping multiple tasks inside list."""
    group = models.ForeignKey(groups_models.Group, on_delete=models.CASCADE, verbose_name=_("group"),
                              blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("list")
        verbose_name_plural = _("lists")
