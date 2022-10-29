from todo.models import Task
from todo.serializers import TaskSerializer
from rest_framework import viewsets , permissions

class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer