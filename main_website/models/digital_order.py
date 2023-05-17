from django.db import models
import uuid
from .giftcard import Giftcard
from django.utils import timezone


class DigitalOrder(models.Model):
    order_number = models.UUIDField(default=uuid.uuid4)
    # for payment
    payment_method = models.CharField(max_length=50)
    email = models.EmailField()
    item_list = models.ManyToManyField(Giftcard)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
