from rest_framework import generics, permissions, authentication, status
from rest_framework.response import Response

from django.contrib.auth import login

from django.contrib.auth.models import User
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer
from .serializers import LoginSerializer
from .serializers import SignupSerializer


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

# class UserSignup(generics.CreateAPIView):


class UserSignup(APIView):
    permission_classes = [permissions.AllowAny]

    serializer_class = SignupSerializer

    def post(self, request, format=None):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"msg": "Registration Successful"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = [permissions.AllowAny]

    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authentication.authenticate(
            username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_200_OK)
            return self._error_response('disabled')
        return self._error_response('invalid')


# class UserLogout():
#     id = 1
