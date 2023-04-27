from django.shortcuts import render
from ..models.giftcard import Giftcard


# using method based view because there are no models required
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
            cart_items[obj] = counter

        context = {"cart_items": cart_items}
    else:
        context = {}

    return render(request, "shopping_cart.html", context)
