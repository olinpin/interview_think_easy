# Task Manager

Task manager is an app, where you can create and edit your tasks

## Installation

1. Change the active directory of your CMD/terminal to this folder (```cd``` on Mac/Linux, ```dir``` on Windows)
2. Run ```pip install -r requirements.txt```, that will install all the dependencies.
3. Run the project with ```python manage.py runserver```

## View functions

```python

# shows all task associated with user, that is currently logged in
index(request)

# when given username and password, will log user in, if username or password is incorrect, it will give invalid credentials error
login_view()

# logs user out
logout_view()

# when user gives username and password, the system will check if the username already exists in the database and if it does, it will give an error, otherwise it will check if the passwords match and if they do, it will create an account
registration()

# when function is called, it extracts the username, title and text, it will create a task and save it, then return the id of the task
addTask()

# when function is called, it switches the 'done' field of the task that was called
change()
```


# Functionalities
When you go to the webpage, you will be redirected to the login window, if you don't have an account yet, you can sign up by clicking the "signup" button, which will redirect you to the registration page. 

When you fill out all the fields on the registration page and click on Sign up, you can go to the login page and log in. 

When you log in, you will be redirected to the homepage.

On homepage you can choose if you want to see the tasks of the logged in user or choose the user from a select. Then you can add tasks. And they will automatically be assigned to the user that is logged in or to the chosen user. When you click on the red X, it will mark the task 'done' and the X will change to a green checkmark, if you click again, it will change back to X etc. When you reload, the tasks which are done, will be at the bottom.

If you click on the Admin, you will be redirected to the admin page, there you can add, change or delete tasks. When you click on Tasks, you can change the state of 'done' field from the list_display.

When you create a new Task, you can choose from the existing users or create a new user. When you go to the User edit, you can add, edit or delete tasks.
