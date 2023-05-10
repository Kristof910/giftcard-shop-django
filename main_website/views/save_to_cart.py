from django.shortcuts import render
from django.shortcuts import redirect


# using method based view because there are no models required
def save_to_cart(request, pk):
    if "shopping_cart" in request.session and request.session.get("shopping_cart"):
        new_list = request.session.get("shopping_cart")
        new_list.append(pk)
        request.session["shopping_cart"] = new_list
    else:
        request.session["shopping_cart"] = [pk]

    return redirect("giftcard-detail", pk=pk)
