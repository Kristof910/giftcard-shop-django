from django.db import models


class ShippingCost(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    cost = models.DecimalField(
        max_digits=10, decimal_places=2, default=20, blank=False, null=False
    )
    active = models.BooleanField(
        default=False,
        help_text="If you activate this shipping, an other shipping method will be deactivated!",
    )

    def save(self, *args, **kwargs):
        if self.active:
            # ensure only one instance is active at a time
            ShippingCost.objects.filter(active=True).update(active=False)
        super(ShippingCost, self).save(*args, **kwargs)

    @classmethod
    def get_active_shipping(cls):
        try:
            return cls.objects.get(active=True)
        # if there are none then it generates a new one
        except cls.DoesNotExist:
            return cls.objects.create(
                name="Generated Default Shipping", cost=20, active=True
            )

    def __str__(self):
        return f"{self.name}, ${self.cost}"
