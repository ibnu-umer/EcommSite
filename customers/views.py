from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def LoginUser(req):
    context={}
    if req.POST and "register" in req.POST.keys():
        context["register"]=True
        try:
            username=req.POST.get("username")
            password=req.POST.get("password")
            email=req.POST.get("email")
            phone=req.POST.get("phone")
            # creates user model
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            # creates customer model
            customer=Customer.objects.create(
                user=user,
                phone=phone
            )
            return redirect("home") # redirects to home page
        except Exception as e:
            if username in str(e):
                messages.error(req, "Invalid Username.")
            else:
                messages.error(req, "Invalid inputs")
                
    elif req.method == "POST" and "login" in req.POST.keys(): # if login clicked
        context["register"]=False
        username=req.POST["username"]
        password=req.POST["password"]
        user=authenticate(username=username, password=password) #authenticate username and password
        if user: # if a user exists with the username and password
            login(req, user)
            return redirect("home")
        else:
            error_msg = "Invalid Credentials"
            messages.error(req, error_msg)

    return render(req, "account.html", context)

def signOut(req):
    logout(req)
    return redirect("login")