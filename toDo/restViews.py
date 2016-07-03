from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from toDo.models import ToDoList, ToDoItem
from toDo.serializers import TodoListSerializer, TodoItemSerializer


@api_view(['GET', 'POST'])
def todolist(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = ToDoList.objects.all()
        serializer = TodoListSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer =TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def todolist_detail(request, pk,format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = ToDoList.objects.get(pk=pk)
    except ToDoList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoListSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoListSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def Item_list(request,id,format=None,):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = ToDoItem.objects.all().filter(name_id__exact=id)
        serializer = TodoItemSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer =TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Item_detail(request, pk,format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = ToDoItem.objects.get(pk=pk)
    except ToDoItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoItemSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoItemSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)