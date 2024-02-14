from django.db import models

from med.models.mix_in import TimeStampedMixin, UUIDMixin
from django.utils.translation import gettext_lazy as _


class Order(TimeStampedMixin, UUIDMixin):
    price = models.DecimalField(_("total price"), decimal_places=2, max_digits=10)

    client = models.ForeignKey("Client", related_name="orders", on_delete=models.CASCADE)
    employee = models.ForeignKey("Employee", related_name="orders", on_delete=models.CASCADE)
    products = models.ManyToManyField("Product", blank=True)

    class Meta:
        db_table = 'public"."orders'
        verbose_name = _("order")
        verbose_name_plural = _("orders")
        app_label = "med"

    def __str__(self):
        return f"<Order id={self.id}>"
