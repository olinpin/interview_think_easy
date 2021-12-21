from django.contrib import admin
from .models import Tasks
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin

# Register your models here.

### TASKS ###

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('text', 'done')
    filter_horizontal = ('user',)

class Inline(admin.TabularInline):
    model = Tasks.user.through
    verbose_name = 'Task'
    verbose_name_plural = "Tasks"

### USERS ###


UserAdmin.inlines = [
    Inline,
]









admin.site.unregister(User)
admin.site.register(User, UserAdmin)
