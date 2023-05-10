from django.shortcuts import render
from ..models.giftcard import Giftcard


def payment_view(request):
    if request.method == "POST":
        pass

    # checks to show or not the shipping details
    show_shipping_details = False
    id_list = request.session.get("shopping_cart")
    filtered_objects = Giftcard.objects.filter(id__in=id_list)
    for obj in filtered_objects:
        if obj.is_digital is False:
            show_shipping_details = True

    context = {"show_shipping_details": show_shipping_details}
    return render(request, "payment.html", context=context)
