from django import template

register=template.Library()

@register.simple_tag(name="total")
def total(cart, discount):
    subtotal=0
    for item in cart.added_items.all():
        subtotal+=item.product.price*item.quantity
    total=(subtotal/100)*(100-discount)
    return total