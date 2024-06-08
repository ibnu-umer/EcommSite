from django.shortcuts import render

# Create your views here.
def Login(req):
    return render(req, "account.html")