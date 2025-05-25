from rest_framework import serializers
from .models import Task, Team
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TeamSerializer(serializers.ModelSerializer):
    #members = UserSerializer(many=True, read_only=True)
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)


    class Meta:
        model = Team
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    
    assigned_to = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'