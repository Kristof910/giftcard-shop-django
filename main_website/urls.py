from django.urls import path
from .views import index_view
from .views import giftcard_detail_view
from .views import contact_view
from .views import shopping_cart_view
from .views import save_to_cart


urlpatterns = [
    path("", index_view.IndexView.as_view(), name="index"),
    path("giftcard/<int:pk>", giftcard_detail_view, name="giftcard-detail"),
    path("contact/", contact_view.contact_view, name="contact"),
    path("cart/", shopping_cart_view, name="shopping-cart"),
    path("add-to-cart/<int:pk>", save_to_cart, name="save-to-cart"),
]
