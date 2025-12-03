from django.urls import path
from .views import about,contact,home,login,registration


urlpatterns = [
    path("",home),
    path("about/",about),
    path("contact/",contact),
    path("login/",login),
    path("registration/",registration),
]
