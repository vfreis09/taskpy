from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.Home.as_view()),
    path('task/', views.CreateTask.as_view()),
    # path('task/<int:pk>/', views.TaskById.as_view()),

    # User auth
    path('login/', views.UserLogin.as_view()),
    # path('signup/', views.UserSignup.as_view()),
]
