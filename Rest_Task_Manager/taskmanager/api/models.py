from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User,related_name="teams")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Done", "Done"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="tasks")
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title