from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator

# Create your views here.
def homePage(req):
    featured_products=Products.objects.order_by("-priority")[:4]
    latest_products=Products.objects.order_by("-id")[:4]
    context={
        "featured_products": featured_products,
        "latest_products": latest_products
    }
    return render(req, "home.html", context)

def products(req):
    products=Products.objects.order_by("-priority") # fetchs all data from database
    product_paginator=Paginator(products, 2) # ( the list of datas, the size of data in a page)
    page=1
    if req.GET:
        page=req.GET.get("page")
    products=product_paginator.get_page(page) # getting the first page from the pages
    return render(req, "products.html", {"products": products})

def show_product(req, pk):
    product=Products.objects.get(pk=pk)
    context={"product":product}
    return render(req, "product_page.html", context)