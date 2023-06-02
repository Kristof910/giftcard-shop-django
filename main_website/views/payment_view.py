from django.shortcuts import render
from django.shortcuts import redirect
from ..models.giftcard import Giftcard
from ..forms.digital_order_form import DigitalOrderForm
from ..models.digital_order import DigitalOrder
from ..forms.order_with_shipping_form import OrderWithShippingForm
from ..models.order_with_shipping import OrderWithShipping


def payment_view(request):
    # checks to show or not the shipping details
    show_shipping_details = False
    id_list = request.session.get("shopping_cart")
    filtered_objects = Giftcard.objects.filter(id__in=id_list)
    for obj in filtered_objects:
        if obj.is_digital is False:
            show_shipping_details = True

    # order with shipping
    if show_shipping_details:
        if request.method == "POST":
            form = OrderWithShippingForm(request.POST)
            if form.is_valid():
                payment_method = form.cleaned_data["payment_method"]
                email = form.cleaned_data["email"]
                name = form.cleaned_data["name"]
                phone = form.cleaned_data["phone"]
                country = form.cleaned_data["country"]
                county = form.cleaned_data["county"]
                address = form.cleaned_data["address"]
                order_with_shipping = OrderWithShipping(
                    payment_method=payment_method,
                    email=email,
                    name=name,
                    phone=phone,
                    country=country,
                    county=county,
                    address=address,
                )
                order_with_shipping.save()
                # search from session all the ids of giftcard instances
                for giftcard_id in request.session.get("shopping_cart"):
                    giftcard_instance = Giftcard.objects.get(pk=giftcard_id)
                    order_with_shipping.item_list.add(giftcard_instance)
            return redirect("payment-end")
        else:
            form = OrderWithShippingForm()

    # digital order
    else:
        if request.method == "POST":
            form = DigitalOrderForm(request.POST)
            if form.is_valid():
                payment_method = form.cleaned_data["payment_method"]
                email = form.cleaned_data["email"]
                digital_order = DigitalOrder(payment_method=payment_method, email=email)
                digital_order.save()
                # search from session all the ids of giftcard instances
                for giftcard_id in request.session.get("shopping_cart"):
                    giftcard_instance = Giftcard.objects.get(pk=giftcard_id)
                    digital_order.item_list.add(giftcard_instance)
            return redirect("payment-end")
        else:
            form = DigitalOrderForm()

    context = {"show_shipping_details": show_shipping_details, "form": form}
    return render(request, "payment.html", context=context)
