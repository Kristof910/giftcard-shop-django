from django.contrib import admin
from .models.giftcard import Giftcard
from .models.giftcard_options.giftcard_region import GiftcardRegion
from .models.giftcard_options.giftcard_type import GiftcardType
from .models.giftcard_options.giftcard_value import GiftcardValue
from .models.contact_message import ContactMessage
from .models.shipping_cost import ShippingCost
from .models.giftcard_code import GiftcardCode
from .models.digital_order import DigitalOrder
from .models.order_with_shipping import OrderWithShipping


class GiftcardAdmin(admin.ModelAdmin):
    list_display = ("type", "region", "value", "is_digital", "price")


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")


class GiftcardCodeAdmin(admin.ModelAdmin):
    list_display = ("giftcard", "for_sale")


class DigitalOrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "created_at", "email", "payment_method")


class OrderWithShippingAdmin(admin.ModelAdmin):
    list_display = ("order_number", "created_at", "email", "payment_method")


admin.site.register(Giftcard, GiftcardAdmin)
admin.site.register(GiftcardRegion)
admin.site.register(GiftcardType)
admin.site.register(GiftcardValue)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(ShippingCost)
admin.site.register(GiftcardCode, GiftcardCodeAdmin)
admin.site.register(DigitalOrder, DigitalOrderAdmin)
admin.site.register(OrderWithShipping, OrderWithShippingAdmin)
