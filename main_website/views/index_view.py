from django.views import generic
from ..models.giftcard import Giftcard


class IndexView(generic.ListView):
    template_name = "index.html"
    model = Giftcard
