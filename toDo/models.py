from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ToDoList(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateField()
    user = models.ForeignKey(User)
    def ___str___(self):
        return self.name

class ToDoItem(models.Model):
    description=models.CharField(max_length=256)
    duedate=models.DateField()
    completed=models.BooleanField(default=False)
    name=models.ForeignKey(ToDoList)
    user = models.ForeignKey(User)