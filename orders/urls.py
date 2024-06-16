from django.urls import path
from orders import views

urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
    path("remove_item/<pk>", views.remove_cart_item, name="remove_item"),
    path("checkout_cart", views.checkout_cart, name="checkout"),
    path("orders", views.show_orders, name='orders')
]