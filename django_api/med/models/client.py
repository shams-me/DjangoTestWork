from django.db import models
from django.utils.translation import gettext_lazy as _

from med.models.mix_in import TimeStampedMixin, UUIDMixin


class Client(TimeStampedMixin, UUIDMixin):
    full_name = models.CharField(_("full name"), max_length=100)
    birth_date = models.DateField(_("birth date"), null=True, blank=True)

    class Meta:
        db_table = 'public"."clients'
        verbose_name = _("client")
        verbose_name_plural = _("clients")
        app_label = "med"

    def __str__(self):
        return self.full_name
