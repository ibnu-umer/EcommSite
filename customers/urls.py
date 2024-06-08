from django.urls import path
from customers import views

urlpatterns = [
    path("loginPage/", views.Login, name="login")
]