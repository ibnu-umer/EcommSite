from django.shortcuts import render, redirect
from products.models import Products
from orders.models import Order, OrderedItem

# Create your views here.
def cart(req):
    user=req.user
    customer=user.customer_profile
    cart_obj=Order.objects.get(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    context={"cart": cart_obj}
    return render(req, "cart.html", context)

def add_to_cart(req):
    if req.POST:
        user=req.user
        customer=user.customer_profile
        quantity=req.POST.get("quantity")
        size=req.POST.get("size")
        product_id=req.POST.get("product_id")
        product=Products.objects.get(pk=product_id)
        cart_obj, created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        ordered_items, createed=OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
            quantity=quantity,
            size=size
        )
        return redirect('cart')