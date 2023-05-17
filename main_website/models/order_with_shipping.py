from django.db import models
import uuid
from .giftcard import Giftcard

class OrderWithShipping(models.Model):
    order_number = models.UUIDField(default=uuid.uuid4, editable=False)
    # for payment
    transaction_id = models.IntegerField()
    name = 
    email = models.EmailField()
    phone = 
    country = 
    county = 
    address = 
    item_list = models.ManyToManyField(Giftcard)


    def __str__(self):
        return f"NO NAMING YET"
