from ..models.giftcard import Giftcard
from ..models.giftcard_options.giftcard_region import GiftcardRegion
from ..models.giftcard_options.giftcard_type import GiftcardType
from ..models.giftcard_options.giftcard_value import GiftcardValue
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# using method based view to pass more then 1 model
def all_cards_view(request):
    giftcards = Giftcard.objects.all()

    # filtering out objects based on form post
    if request.method == "POST":
        if request.POST.getlist("region[]"):
            giftcards = giftcards.filter(
                region__name__in=request.POST.getlist("region[]")
            )
        if request.POST.getlist("type[]"):
            giftcards = giftcards.filter(type__name__in=request.POST.getlist("type[]"))
        if request.POST.getlist("values[]"):
            giftcards = giftcards.filter(
                value__value__in=request.POST.getlist("values[]")
            )
        if request.POST.getlist("delivery[]"):
            giftcards = giftcards.filter(
                is_digital__in=request.POST.getlist("delivery[]")
            )

    regions = GiftcardRegion.objects.all()
    types = GiftcardType.objects.all()
    values = GiftcardValue.objects.all()

    # pagination (manual)
    paginator = Paginator(giftcards, 6)
    page = request.GET.get("page")
    try:
        giftcards = paginator.page(page)
    except PageNotAnInteger:
        giftcards = paginator.page(1)
    except EmptyPage:
        giftcards = paginator.page(paginator.num_pages)

    context = {
        "giftcards": giftcards,
        "regions": regions,
        "types": types,
        "values": values,
    }

    return render(request, "all_cards.html", context)
