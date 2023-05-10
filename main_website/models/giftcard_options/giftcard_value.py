from django.db import models
from .giftcard_region import GiftcardRegion


class GiftcardValue(models.Model):
    value = models.PositiveIntegerField(default=10, blank=False, null=False)

    def __str__(self):
        return str(self.value)

    class Meta:
        ordering = ["value"]
