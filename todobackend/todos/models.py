# In models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='todos')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('complete', 'Complete')], default='pending')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
