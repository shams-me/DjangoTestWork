from django.db import models

from med.models.mix_in import TimeStampedMixin, UUIDMixin
from django.utils.translation import gettext_lazy as _


class Product(TimeStampedMixin, UUIDMixin):
    name = models.CharField(_("name"), max_length=255)
    quantity = models.IntegerField(_("quantity"), default=1)
    price = models.DecimalField(_("price"), default=1.0, decimal_places=2, max_digits=10)

    class Meta:
        db_table = 'public"."products'
        verbose_name = _("product")
        verbose_name_plural = _("products")
        app_label = "med"

    def __str__(self):
        return self.name
