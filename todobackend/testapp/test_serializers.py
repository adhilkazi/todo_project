# In tests/test_serializers.py

from django.test import TestCase
from todos.serializers import ProjectSerializer, TodoSerializer

class ProjectSerializerTestCase(TestCase):
    def test_valid_title(self):
        serializer = ProjectSerializer(data={'title': 'Test Project'})
        self.assertTrue(serializer.is_valid())

    def test_invalid_title(self):
        serializer = ProjectSerializer(data={'title': '1234'})
        self.assertFalse(serializer.is_valid())

class TodoSerializerTestCase(TestCase):
    def test_valid_data(self):
        serializer = TodoSerializer(data={'description': 'Test Todo', 'status': 'pending'})
        self.assertTrue(serializer.is_valid())

    def test_invalid_data(self):
        serializer = TodoSerializer(data={'description': 'Test Todo', 'status': 'invalid'})
        self.assertFalse(serializer.is_valid())
