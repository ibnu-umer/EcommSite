from django.shortcuts import render
from . models import Products
from django.core.paginator import Paginator

# Create your views here.
def homePage(req):
    return render(req, "home.html")

def products(req):
    products=Products.objects.all() # fetchs all data from database
    product_paginator=Paginator(products, 2) # ( the list of datas, the size of data in a page)
    page=1
    if req.GET:
        page=req.GET.get("page")
    products=product_paginator.get_page(page) # getting the first page from the pages
    return render(req, "products.html", {"products": products})

def show_product(req):
    return render(req, "product_page.html")