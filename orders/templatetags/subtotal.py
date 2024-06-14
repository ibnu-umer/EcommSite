from django import template

register=template.Library()

@register.simple_tag(name="subtotal")
def subtotal(cart):
    sub_total=0
    for item in cart.added_items.all():
        sub_total+=item.product.price*item.quantity
    return sub_total