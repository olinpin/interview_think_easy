from django.http import HttpResponseRedirect, JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from .models import Tasks
import json
from django.core import serializers

# Create your views here.

@login_required(login_url='tasks:login')
def index(request):
    # get all tasks that are associated with this user and make them in order
    #tasks_model = Tasks.objects.all().filter(user=request.user).order_by("done")
    tasks_model = Tasks.objects.all().order_by("done")
    users = User.objects.all()
    return render(request, 'Task_Manager/index.html', {
        "tasks": tasks_model,
        "users": users,
    })

def login_view(request):
    if request.method == "POST":
        # get the username and password
        username = request.POST["username"].lower()
        password = request.POST["password"]
        # make sure they are correct
        user = authenticate(request, username='oliverhnat', password='Olinpin2393')
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

def registration(request):
    if request.method == "POST":
        # extract the username and password
        username = request.POST["username"].lower()
        password = request.POST["password"]
        password2 = request.POST["password2"]
        try:
            # check if the username is already used
            user = User.objects.get(username=username)

            return render(request, "task_manager/register.html",{
                "message": "This username already exists",
                "bad": "yes",
            })
        except:
            # check again if passwords match
            if password == password2:
                # create the user with username and password
                User.objects.create_superuser(username=username, password=password)
                return render(request, "task_manager/register.html",{
                    "message": "Your registration is saved, you can now log in",
                    "good": "yes",
                })
            else:
                return render(request, "task_manager/register.html",{
                    "message": "There was an error, please try again",
                    "bad": "yes",
                })
    else:
        return render(request, "task_manager/register.html")

### FUNCTIONS ###

# this functions creates a task based on the information given
def addTask(request):
    if request.method == "POST":
        # get the username, text and find the user in the User model
        username = request.POST["username"]
        title = request.POST["title"]
        text = request.POST["text"]
        user = User.objects.get(username=username)
        # create task and set the value of text and then user
        task = Tasks()
        task.text = text
        task.title = title
        task.user = user
        task.save()
        return JsonResponse({
            "code":400,
            "id": task.id
            })

# this function changes the 'done' field of task based on id
def change(request):
    if request.method == "POST":
        id = request.POST['id']
        task = Tasks.objects.get(id=id)
        task.done = not task.done
        task.save()
        return JsonResponse({
            "code":400,
            "done": task.done,
            })
