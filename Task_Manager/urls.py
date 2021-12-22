from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    ### PAGES ###
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.registration, name="registration"),

    ### FUNCTIONS ###
    path('addTask', views.addTask, name="addTask"),
    path('change', views.change, name="change")
]