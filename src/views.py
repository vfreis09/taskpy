from rest_framework import generics, permissions, authentication

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from .models import Task
from .serializers import TaskSerializer
from .serializers import UserSerializer


class Home(generics.ListAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user)


class CreateTask(generics.CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskById(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Bellow this nothing is working

# class UserLogin(generics.CreateAPIView):
#     permission_classes = [permissions.AllowAny]


# class UserSignup(generics.CreateAPIView):
#     permission_classes = [permissions.AllowAny]

#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserLogout():
#     id = 1
