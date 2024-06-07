from django.urls import path
# from . import settings
# from django.conf.urls import static
from products import views

urlpatterns = [
    path("products/", views.products, name="products")
]