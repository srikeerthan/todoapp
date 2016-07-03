from rest_framework import serializers

from toDo.models import ToDoList, ToDoItem


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('id', 'name', 'created')


class TodoItemSerializer(serializers.ModelSerializer):
    # li_name = serializers.RelatedField(source='name', read_only=True)
    class Meta:
        model = ToDoItem
        fields = ('id','description','duedate','completed','name')