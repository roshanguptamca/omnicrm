from .models import Session, Task, Log
from rest_framework import serializers


class SessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = '__all__'