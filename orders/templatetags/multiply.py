from django import template

register=template.Library()

@register.simple_tag(name="multiply")
def multiply(x, y):
    return x*y