# In tests/test_views.py

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from todos.views import ProjectListCreate, TodoListCreate
from todos.models import Project, Todo

class ProjectListViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_project_list(self):
        request = self.factory.get('/projects/')
        request.user = self.user
        response = ProjectListCreate.as_view()(request)
        self.assertEqual(response.status_code, 200)

class TodoListViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.project = Project.objects.create(title="Test Project")

    def test_todo_list(self):
        request = self.factory.get(f'/projects/{self.project.id}/todos/')
        request.user = self.user
        response = TodoListCreate.as_view()(request, project_pk=self.project.id)
        self.assertEqual(response.status_code, 200)
