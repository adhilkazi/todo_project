from django.urls import path
from . import views

urlpatterns = [
    # Endpoints for projects
    path('projects/', views.ProjectListCreate.as_view(), name='projectlist'),  # List all projects
    path('projects/create/', views.ProjectListCreate.as_view(), name='projectcreate'),  # Create a new project
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='projectdetail'),  # Retrieve, update, delete a project

    # Endpoints for todos
    path('projects/<int:project_pk>/todos/', views.TodoListCreate.as_view(), name='todolist'),  # List all todos for a project
    path('projects/<int:project_pk>/todos/create/', views.TodoListCreate.as_view(), name='todocreate'),  # Create a new todo for a project
    path('projects/<int:project_pk>/todos/<int:pk>/', views.TodoDetail.as_view(), name='tododetail'),  # Retrieve, update, delete a todo
]
