from django.db import models
from .giftcard_region import GiftcardRegion


class GiftcardValue(models.Model):
    value = models.PositiveIntegerField()

    def __str__(self):
        return str(self.value)
