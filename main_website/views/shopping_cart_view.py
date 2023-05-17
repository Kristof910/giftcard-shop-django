from django.shortcuts import render
from ..models.giftcard import Giftcard
from ..models.shipping_cost import ShippingCost


# using method based view because there are multiple models required
def shopping_cart_view(request):
    if "shopping_cart" in request.session and request.session.get("shopping_cart"):
        id_list = request.session.get("shopping_cart")
        filtered_objects = Giftcard.objects.filter(id__in=id_list)

        # making a dictionary with products + amount of ordered
        cart_items = {}
        for obj in filtered_objects:
            counter = 0
            for i in id_list:
                if i == obj.id:
                    counter += 1
            cart_items[obj] = {"amount": counter, "total_price": 0}

        # shipping cost
        shipping = 0
        for obj in cart_items:
            if obj.is_digital is False:
                shipping = ShippingCost.get_active_shipping().cost

        # calculating per item total price and final price
        final_price = 0
        for key, value in cart_items.items():
            value["total_price"] = key.price * value["amount"]
            final_price += value["total_price"]

        final_price += shipping

        context = {
            "cart_items": cart_items,
            "final_price": final_price,
            "shipping": shipping,
        }
    else:
        context = {}

    return render(request, "shopping_cart.html", context)
