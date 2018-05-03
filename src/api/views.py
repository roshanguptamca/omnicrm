from django.shortcuts import render
from rest_framework import generics
from .models import Session
from .serializers import SessionSerializer


# Create your views here.
class SessionView(generics.ListCreateAPIView):
    """
    Session api
    endpoint : /session
    """
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def perform_create(self, serializer):
        serializer.save()