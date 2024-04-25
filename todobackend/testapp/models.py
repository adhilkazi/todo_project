# In tests/test_models.py

from django.test import TestCase
from todos.models import Project, Todo

class ProjectModelTestCase(TestCase):
    def test_project_creation(self):
        project = Project.objects.create(title="Test Project")
        self.assertEqual(project.title, "Test Project")

class TodoModelTestCase(TestCase):
    def test_todo_creation(self):
        project = Project.objects.create(title="Test Project")
        todo = Todo.objects.create(description="Test Todo", project=project)
        self.assertEqual(todo.description, "Test Todo")

