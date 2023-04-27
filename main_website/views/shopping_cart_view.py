from django.shortcuts import render


# using method based view because there are no models required
def shopping_cart_view(request):
    if "shopping_cart" in request.session and request.session.get("shopping_cart"):
        context = {"cart_items": request.session.get("shopping_cart")}
    else:
        context = {"cart_items": ["Your shopping cart is empty!"]}

    return render(request, "shopping_cart.html", context)
