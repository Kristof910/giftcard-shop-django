from django.shortcuts import render
from ..models.giftcard_code import GiftcardCode
from ..models.digital_order import DigitalOrder
from ..models.giftcard import Giftcard


def payment_end_view(request):
    code_list = []
    # getting all ordered code
    for giftcard_id in request.session.get("shopping_cart"):
        giftcard_object = Giftcard.objects.get(pk=giftcard_id)
        ordered_giftcard_code = GiftcardCode.objects.filter(
            giftcard=giftcard_object, for_sale=True
        ).first()
        code_list.append(ordered_giftcard_code)
        # marking the code as sold
        ordered_giftcard_code.for_sale = False
        ordered_giftcard_code.save()
        # clearing shopping cart
        request.session["shopping_cart"] = []

    context = {"code_list": code_list}
    return render(request, "payment_end.html", context=context)
