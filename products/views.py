from django.shortcuts import render

# Create your views here.
def homePage(req):
    return render(req, "index.html")

def products(req):
    return render(req, "products.html")