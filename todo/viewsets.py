from rest_framework import viewsets

from todo.models import Todo, TodoCategory
from todo.serializers import TodoSerializer, TodoCategorySerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoCategoryViewSet(viewsets.ModelViewSet):
    queryset = TodoCategory.objects.all()
    serializer_class = TodoCategorySerializer
