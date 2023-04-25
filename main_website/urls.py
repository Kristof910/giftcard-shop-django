from django.urls import path
from .views import index_view
from .views import giftcard_detail_view
from .views import contact_view


urlpatterns = [
    path("", index_view.IndexView.as_view(), name="index"),
    path("giftcard/<int:pk>", giftcard_detail_view, name="giftcard-detail"),
    path("contact/", contact_view.contact_view, name="contact"),
]
