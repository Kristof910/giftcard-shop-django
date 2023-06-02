from django.db import models
import uuid
from .giftcard import Giftcard
from django.utils import timezone


class OrderWithShipping(models.Model):
    order_number = models.UUIDField(default=uuid.uuid4, editable=False)
    payment_method = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    item_list = models.ManyToManyField(Giftcard)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
