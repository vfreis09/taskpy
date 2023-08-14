from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('task/', views.CreateTask.as_view()),
    path('task/<int:pk>/', views.TaskById.as_view()),

    # User auth
    path('signup/', views.UserSignup.as_view()),
    path('login/', views.UserLogin.as_view()),
    path('logout/', views.UserLogout.as_view()),
]
