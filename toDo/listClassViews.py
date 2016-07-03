from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import Http404
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from toDo.models import ToDoList
@method_decorator(login_required,name='dispatch')
class todo_ListView(ListView):
    model = ToDoList
    context_object_name = "todolist"

    def get_queryset(self):
        return ToDoList.objects.filter(user=self.request.user)

    template_name = "todlist.html"

@method_decorator(login_required,name='dispatch')
class todo_DetailView(DetailView):
    model = ToDoList
    def get_object(self, queryset=None):
        id_val = self.kwargs.get("pk")
        i = ToDoList.objects.get(id=id_val)
        j = i.user
        id2 = self.request.user
        if j == id2:
            return ToDoList.objects.get(id=id_val)
        else:
            raise Http404("you are not authenticated user")

@method_decorator(login_required,name='dispatch')
class todo_CreateView(CreateView):
    model=ToDoList
    context_object_name = "jails"
    fields = ['name','created']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(todo_CreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("todo-lists")

@method_decorator(login_required,name='dispatch')
class todo_DeletelView(DeleteView):
    model=ToDoList

    def get_object(self, queryset=None):
        # return super(CCUpdateView, self).get_object(queryset)
        id_val = self.kwargs.get("pk")
        i = ToDoList.objects.get(id=id_val)
        j = i.user
        id2 = self.request.user
        if j == id2:
            return ToDoList.objects.get(id=id_val)
        else:
            raise Http404("you are not authenticated user")

    def get_success_url(self):
        return reverse("todo-lists")

@method_decorator(login_required,name='dispatch')
class todo_UpdateView(UpdateView):
    model=ToDoList
    fields = ['name','created']

    def get_object(self, queryset=None):
        # return super(CCUpdateView, self).get_object(queryset)
        id_val = self.kwargs.get("pk")
        i = ToDoList.objects.get(id=id_val)
        j = i.user
        id2 = self.request.user
        if j == id2:
            return ToDoList.objects.get(id=id_val)
        else:
            raise Http404("you are not authenticated user")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(todo_UpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("todo-lists")