from django.urls import path
from customers import views

urlpatterns = [
    path("loginPage/", views.LoginUser, name="login"),
    path("logout/", views.signOut, name="logout")
]