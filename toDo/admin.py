from django.contrib import admin

# Register your models here.

from .models import ToDoList,ToDoItem
admin.site.register([ToDoList,ToDoItem])