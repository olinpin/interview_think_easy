from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, 'Task_Manager/index.html')


def login_view(request):
    if request.method == "POST":
        # get the username and password
        username = request.POST["username"]
        password = request.POST["password"]
        # make sure they are correct
        user = authenticate(request, username=username, password=password)
        # if credentials are correct, log user in
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            # invalid credentials
            return render(request, "Task_Manager/login.html", {
                "message": "Invalid credentials",
                "bad": "yes"
            })
    return render(request, "Task_Manager/login.html")


def logout_view(request):
    # logs user out
    logout(request)
    return render(request, "Task_Manager/login.html",{
        "message": "You've been logout.",
        "good": "yes",
    })