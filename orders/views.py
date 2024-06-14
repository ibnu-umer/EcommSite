from django.shortcuts import render, redirect
from products.models import Products
from orders.models import Order, OrderedItem
from django.contrib import messages

# Create your views here.
def cart(req):
    if req.POST: # to not show the form resubmission confirmation
        return redirect('cart')
    user=req.user
    customer=user.customer_profile
    try:
        cart_obj=Order.objects.get(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        context={"cart": cart_obj, "username": user}
    except:
        context={"empty_msg": "The Cart is Empty."}
    return render(req, "cart.html", context)

def my_orders(req):
    return render(req, "ordered_items_page.html")

def add_to_cart(req):
    if req.POST:
        user=req.user
        customer=user.customer_profile
        quantity=int(req.POST.get("quantity"))
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
            size=size
        )
        if created:
            ordered_items.quantity=quantity
            ordered_items.save()
        else:
            ordered_items.quantity=ordered_items.quantity+quantity
            ordered_items.save()
        return redirect('cart')
    
def remove_cart_item(req, pk):
    item=OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')

def checkout_cart(req):
    if req.POST:
        try:
            user=req.user
            customer=user.customer_profile      
            total=float(req.POST.get("total"))
            order_obj=Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status=Order.ORDER_CONFIRMED
                order_obj.save()
                status_msg="Ordered successfully."
                messages.success(req, status_msg)
                return redirect('my_orders')
            else:
                status_msg="Order cannot be processed."
                messages.error(req, status_msg)
                return redirect("my_orders")
        except Exception as e:
            status_msg=str(e)
            print(status_msg)
            messages.error(req, status_msg)
            return redirect('cart')
    return redirect('cart')