from django.shortcuts import render
from ..models.giftcard import Giftcard
from ..models.giftcard_code import GiftcardCode


# using method based view for easier access of type.description field
def giftcard_detail_view(request, pk):
    # checking cart count for proper error message
    if "shopping_cart" in request.session and request.session.get("shopping_cart"):
        cart_list = request.session.get("shopping_cart")
        cart_stock = cart_list.count(pk)
    else:
        cart_stock = 0

    giftcard = Giftcard.objects.get(pk=pk)
    total_stock = GiftcardCode.objects.filter(giftcard=giftcard, for_sale=True).count()
    context = {
        "giftcard": giftcard,
        "pk": pk,
        "total_stock": total_stock,
        "cart_stock": cart_stock,
    }
    return render(request, "giftcard_detail.html", context)
