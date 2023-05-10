from django.shortcuts import render
from django.shortcuts import redirect


# using method based view because there are no models required
def delete_item_from_cart(request, pk):
    session_list = request.session.get("shopping_cart")
    session_list.remove(pk)
    request.session["shopping_cart"] = session_list

    return redirect("shopping-cart")
