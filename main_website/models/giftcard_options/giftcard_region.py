from django.db import models


class GiftcardRegion(models.Model):
    name = models.CharField(max_length=30, default="Europe", blank=False, null=False)
    currency = models.CharField(max_length=6, default="€", blank=False, null=False)

    def __str__(self):
        return self.name
