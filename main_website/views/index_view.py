from django.views import generic
from ..models.giftcard import Giftcard
from django.db.models import Count


class IndexView(generic.ListView):
    template_name = "index.html"
    model = Giftcard
    paginate_by = 6
