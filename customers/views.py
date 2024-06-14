from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def LoginUser(req):
    context={}
    error_detail=None
    if req.POST and "register" in req.POST.keys():
        context["register"]=True # not to change the pages when clicking login

        username=req.POST.get("username")
        password=req.POST.get("password")
        email=req.POST.get("email")
        phone=req.POST.get("phone")
        address=req.POST.get("address")
        
        try:
            # creates user model
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            user_created=True
            try:
                # creates customer model
                customer=Customer.objects.create(
                    user=user,
                    phone=phone,
                    address=address,
                    name=user
                )
                user=authenticate(username=username, password=password)
                if user:
                    login(req, user)
                    return redirect("home") # redirects to home page
            except Exception as e:
                print(e)
                user.delete()
                messages.error(req, "Invalid inputs")
                error_detail=str(e)
                
        except Exception as e:
            messages.error(req, "Invalid Username.")
                
                
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

    context["error_detail"] = error_detail
    return render(req, "account.html", context)

def signOut(req):
    logout(req)
    return redirect("login")