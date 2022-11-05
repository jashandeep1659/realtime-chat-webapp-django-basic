from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def Home(request):
    return render(request, "index.html")


def Signup(request):
    logout(request)
    return redirect("login")
    return render(request, "logout.html")


def Login(request):
    isLogin = False
    if request.user.is_authenticated:
        isLogin = True
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username and password:
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("login")
    return render(request, "login.html", {"isLogin": isLogin})


def Chat(request):
    return render(request, "chat.html")
