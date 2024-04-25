# In serializers.py

from rest_framework import serializers
from .models import Project, Todo
from django.contrib.auth.models import User
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password field is write-only
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'created_date']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'project', 'description', 'status', 'created_date', 'updated_date']


        # In serializers.py



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'created_date']

    def validate_title(self, value):
        # Add your validation logic here
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'description', 'status', 'created_date', 'updated_date']

    def validate(self, data):
        # Add your validation logic here
        if data['status'] == 'complete' and not data['updated_date']:
            raise serializers.ValidationError("Updated date is required for completed todos.")
        return data

# serializers.py



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'  # Serialize all fields

