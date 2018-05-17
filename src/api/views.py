from rest_framework import viewsets
from .models import Session, Task, Log
from .serializers import SessionSerializer, LogSerializer, TaskSerializer


# Create Session views here.
class SessionViewSet(viewsets.ModelViewSet):
    """
    Session api
    endpoint : /session
    """
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def perform_create(self, serializer):
        serializer.save()


# Create Task views here.
class TaskViewSet(viewsets.ModelViewSet):
    """
    Session api
    endpoint : /task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save()


# Create Log views here.
class LogViewSet(viewsets.ModelViewSet):
    """
    Session api
    endpoint : /log
    """
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    def perform_create(self, serializer):
        serializer.save()