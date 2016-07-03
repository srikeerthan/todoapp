"""toDoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers

from toDo import views, listClassViews, itemClassViews, restViews

# router = routers.DefaultRouter()
# router.register(r'users', restViews.)
# router.register(r'groups', restViews.GroupViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('django.contrib.auth.urls')),
    url(r'^$',views.home),
    url(r'^todolist/$',listClassViews.todo_ListView.as_view(),name="todo-lists"),
    url(r'todolist/create$', listClassViews.todo_CreateView.as_view()),
    url(r'todolist/(?P<pk>[0-9]+)/delete$', listClassViews.todo_DeletelView.as_view()),
    url(r'todolist/(?P<pk>[0-9]+)$',listClassViews.todo_DetailView.as_view(),name="todo-item"),
     url(r'todolist/(?P<pk>[0-9]+)/update$',listClassViews.todo_UpdateView.as_view()),
    url(r'todolist/(?P<id>[0-9]+)/create$',itemClassViews.item_CreateView.as_view()),
    url(r'todoitem/(?P<id>[0-9]+)$',itemClassViews.item_ListView.as_view(),name="todo-items"),
    url(r'todolist/(?P<id>[0-9]+)/(?P<pk>[0-9]+)/update', itemClassViews.item_UpdateView.as_view()),
    url(r'todolist/(?P<id>[0-9]+)/(?P<pk>[0-9]+)/delete', itemClassViews.item_DeleteView.as_view()),
    url(r'^api/todolists/$', restViews.todolist),
    url(r'^api/todolists/(?P<pk>[0-9]+)/$', restViews.todolist_detail),
    url(r'^api/todolists/(?P<id>[0-9]+)/todoitems/$', restViews.Item_list),
    url(r'^api/todolists/[0-9]+/todoitems/(?P<pk>[0-9]+)$', restViews.Item_detail),

]

