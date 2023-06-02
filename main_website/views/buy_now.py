from django.shortcuts import render
from django.shortcuts import redirect


# using method based view because there are no models required
def buy_now(request, pk):
    request.session["shopping_cart"] = [pk]

    return redirect("shopping-cart")
