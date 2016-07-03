from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from models import *
from django.template import loader
from django.forms import inlineformset_factory
# def create(request):
#     BookFormSet = inlineformset_factory(ToDoList, ToDoItem, fields=('description','duedate','completed',))
#     author = ToDoList.objects.get(name='Mike Royko')
#     formset = BookFormSet(instance=author)

def test(request):
    lis=ToDoList.objects.all()
    lo=loader.get_template('todlist.html')
    r=lo.render(context={'t_list':lis})
    return HttpResponse(r)

def items(request,id):
    lis = ToDoItem.objects.filter(name_id=id)
    lo = loader.get_template('todoitems.html')
    r = lo.render(context={'t_items': lis})
    return HttpResponse(r)

def home(request):
    return render(request, 'home.html')
