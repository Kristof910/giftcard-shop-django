from django.db import models


class GiftcardType(models.Model):
    name = models.CharField(max_length=50, default="Apple", blank=False, null=False)
    description = models.TextField(
        default="This is a description for Apple Giftcard.", blank=True, null=True
    )

    def __str__(self):
        return self.name
