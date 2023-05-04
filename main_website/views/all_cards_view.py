from ..models.giftcard import Giftcard
from ..models.giftcard_options.giftcard_region import GiftcardRegion
from ..models.giftcard_options.giftcard_type import GiftcardType
from ..models.giftcard_options.giftcard_value import GiftcardValue
from django.shortcuts import render


# using method based view to pass more then 1 model
def all_cards_view(request):
    if request.method == "POST":
        print("HELLO")
        selected_regions = request.POST.getlist("region[]")
        print("REGION: ", selected_regions)
        selected_types = request.POST.getlist("type[]")
        selected_values = request.POST.getlist("values[]")
        selected_delivery_methods = request.POST.getlist("delivery[]")

        giftcards = Giftcard.objects.filter(
            region__name__in=selected_regions,
            type__name__in=selected_types,
            value__value__in=selected_values,
            is_digital__in=selected_delivery_methods,
        )
    else:
        giftcards = Giftcard.objects.all()

    regions = GiftcardRegion.objects.all()
    types = GiftcardType.objects.all()
    values = GiftcardValue.objects.all()

    context = {
        "giftcards": giftcards,
        "regions": regions,
        "types": types,
        "values": values,
    }

    return render(request, "all_cards.html", context)
