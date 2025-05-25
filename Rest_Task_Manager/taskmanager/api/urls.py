from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view()),
    path('teams/', views.TeamListCreateView.as_view()),
    path('teams/<int:pk>/', views.TeamDetailView.as_view()),
    path('users/', views.UserListView.as_view()),
]