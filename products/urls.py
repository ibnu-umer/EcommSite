from django.urls import path
from products import views

urlpatterns = [
    path("", views.homePage, name="home"),
    path("products/", views.products, name="products"),
    path("show_product/<pk>", views.show_product, name="product")
]