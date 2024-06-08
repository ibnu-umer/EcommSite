from django.urls import path
from themes import views

urlpatterns = [
    path("themes/", views.themes, name="themes")
]