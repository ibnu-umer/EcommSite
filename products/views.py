from django.shortcuts import render

# Create your views here.
def homePage(req):
    return render(req, "home.html")

def products(req):
    return render(req, "products.html")

def show_product(req):
    return render(req, "product_page.html")