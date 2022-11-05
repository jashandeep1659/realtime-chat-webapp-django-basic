from django.urls import path
from .views import *

urlpatterns = [
    path("", Home, name="Home"),
    path("logout", Signup, name="signup"),
    path("login", Login, name="login"),
    path("chat", Chat, name="chat"),
]
