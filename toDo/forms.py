from django.forms import ModelForm
from toDo.models import ToDoList

class ContactAjaxForm(ModelForm):
    class Meta:
        model=ToDoList
