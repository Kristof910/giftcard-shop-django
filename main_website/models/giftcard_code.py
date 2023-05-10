from django.db import models
from .giftcard import Giftcard


class GiftcardCode(models.Model):
    giftcard = models.ForeignKey(Giftcard, on_delete=models.SET_NULL, null=True)
    code = models.CharField(
        max_length=14, default="0000-0000-0000", blank=False, null=False
    )
    for_sale = models.BooleanField(
        default=True,
        help_text="If this is not active, it means it was sold!",
    )

    def __str__(self):
        return f"NAME: {self.giftcard} | FOR SALE: {self.for_sale}"
