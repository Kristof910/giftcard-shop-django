from django.db import models


class GiftcardRegion(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    # have image with ID

    def __str__(self):
        return self.name
