from django.db import models
from main_website.models.giftcard_options.giftcard_region import GiftcardRegion
from main_website.models.giftcard_options.giftcard_type import GiftcardType
from main_website.models.giftcard_options.giftcard_value import GiftcardValue


class Giftcard(models.Model):
    type = models.ForeignKey(GiftcardType, on_delete=models.SET_NULL, null=True)
    value = models.ForeignKey(GiftcardValue, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(GiftcardRegion, on_delete=models.SET_NULL, null=True)
    is_digital = models.BooleanField(default=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type} {self.region} {self.value}"
