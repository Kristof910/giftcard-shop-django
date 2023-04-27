from django.shortcuts import render
from ..models.giftcard import Giftcard


# using method based view for easier access of type.description field
def giftcard_detail_view(request, pk):
    giftcard = Giftcard.objects.get(pk=pk)
    context = {"giftcard": giftcard, "pk": pk}
    return render(request, "giftcard_detail.html", context)
