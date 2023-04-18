from django.db import models


class GiftcardValue(models.Model):
    name = models.CharField(max_length=10, blank=False, null=False)
    value = models.PositiveIntegerField()
