from django.urls import path
from .views.index_view import IndexView
from .views import giftcard_detail_view
from .views.contact_view import contact_view
from .views import shopping_cart_view
from .views import save_to_cart
from .views.delete_item_from_cart import delete_item_from_cart
from .views.all_cards_view import all_cards_view


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("giftcard/<int:pk>", giftcard_detail_view, name="giftcard-detail"),
    path("contact/", contact_view, name="contact"),
    path("cart/", shopping_cart_view, name="shopping-cart"),
    path("add-to-cart/<int:pk>", save_to_cart, name="save-to-cart"),
    path(
        "delete-from-cart/<int:pk>",
        delete_item_from_cart,
        name="delete-from-cart",
    ),
    path("all-cards", all_cards_view, name="all-cards"),
]
