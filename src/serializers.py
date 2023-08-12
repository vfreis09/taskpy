from django.contrib.auth.models import User
from .models import Task
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'tasks']


class AuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
