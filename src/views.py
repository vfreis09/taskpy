from rest_framework import generics, permissions, authentication
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from .models import Task
from .serializers import TaskSerializer
from .serializers import UserSerializer

# class Home(generics.RetrieveAPIView):
#     #I want to get a list of tasks based on user id
#     authentication_classes = [authentication.SessionAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
    
#     def get(self,request, pk):
#         queryset = Task.objects.get(pk=pk)
#         serializer_class = TaskSerializer
    
    

class CreateTask(generics.CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
 

# class TaskById(generics.RetrieveUpdateDestroyAPIView):
#     authentication_classes = [authentication.SessionAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


class UserLogin(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]


class UserSignup(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserLogout():
#     id = 1
