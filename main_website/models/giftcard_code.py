from django.db import models
from .giftcard import Giftcard


class GiftcardCode(models.Model):
    giftcard = models.ForeignKey(Giftcard, on_delete=models.SET_NULL, null=True)
    code = models.CharField(
        max_length=14, default="0000-0000-0000", blank=False, null=False
    )

    def __str__(self):
        return str(self.giftcard)
