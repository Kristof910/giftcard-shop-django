from django.contrib import admin
from .models.giftcard import Giftcard
from .models.giftcard_options.giftcard_region import GiftcardRegion
from .models.giftcard_options.giftcard_type import GiftcardType
from .models.giftcard_options.giftcard_value import GiftcardValue

admin.site.register(Giftcard)
admin.site.register(GiftcardRegion)
admin.site.register(GiftcardType)
admin.site.register(GiftcardValue)
