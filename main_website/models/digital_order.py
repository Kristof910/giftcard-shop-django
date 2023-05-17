from django.db import models
import uuid
from .giftcard import Giftcard


class DigitalOrder(models.Model):
    order_number = models.UUIDField(default=uuid.uuid4)
    # for payment
    payment_method = models.CharField(max_length=50)
    email = models.EmailField()
    item_list = models.ManyToManyField(Giftcard)

    def __str__(self):
        return f"NO NAMING YET"
