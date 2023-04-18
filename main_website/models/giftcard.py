from django.db import models
from main_website.models.giftcard_options.giftcard_region import GiftcardRegion
from main_website.models.giftcard_options.giftcard_type import GiftcardType
from main_website.models.giftcard_options.giftcard_value import GiftcardValue


class Giftcard(models.Model):
    type = models.ManyToManyField(GiftcardType)
    value = models.ManyToManyField(GiftcardValue)
    region = models.ManyToManyField(GiftcardRegion)
    is_digital = models.BooleanField(default=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_stock = models.PositiveIntegerField()
