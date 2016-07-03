from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import Http404
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from toDo.models import ToDoItem

@method_decorator(login_required,name='dispatch')
class item_ListView(ListView):
    model=ToDoItem

    def get_queryset(self):
        return ToDoItem.objects.filter(user=self.request.user)

@method_decorator(login_required,name='dispatch')
class item_CreateView(CreateView):
    model=ToDoItem
    fields = ['description','duedate','completed']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.name_id=self.kwargs['id']
        return super(item_CreateView, self).form_valid(form)


    def get_success_url(self):
            return reverse('todo-lists')

@method_decorator(login_required,name='dispatch')
class item_UpdateView(UpdateView):
    model = ToDoItem
    fields = ['description', 'duedate', 'completed']

    def get_object(self, queryset=None):
        # return super(CCUpdateView, self).get_object(queryset)
        id_val = self.kwargs.get("pk")
        i = ToDoItem.objects.get(id=id_val)
        j = i.user
        id2 = self.request.user
        if j == id2:
            return ToDoItem.objects.get(id=id_val)
        else:
            raise Http404("you are not authenticated user")

    def form_valid(self, form):
        form.instance.name_id = self.kwargs['id']
        form.instance.user = self.request.user
        return super(item_UpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('todo-lists')

@method_decorator(login_required,name='dispatch')
class item_DeleteView(DeleteView):
    model=ToDoItem

    def get_object(self, queryset=None):
        # return super(CCUpdateView, self).get_object(queryset)
        id_val = self.kwargs.get("pk")
        i = ToDoItem.objects.get(id=id_val)
        j = i.user
        id2 = self.request.user
        if j == id2:
            return ToDoItem.objects.get(id=id_val)
        else:
            raise Http404("you are not authenticated user")

    def get_success_url(self):
        return reverse('todo-lists')
