# schedule/models.py
# blenda jashari - w19760609 
# student4
from django.db import models

from django.contrib.auth.models import User
# Importing necessary modules from Django framework


class Meeting(models.Model):
    # Django ORM used to define database tables as Python classes
    # Model represents a database table (covered in Django lectures)
    title = models.CharField(max_length=200)
    # Stores meeting title
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    # Stores meeting host name
    team_or_members = models.CharField(max_length=200)
    # Stores team name or individual members involved in the meeting
    meeting_date = models.DateField()
    # Stores meeting date
    meeting_time = models.TimeField()
    # Stores meeting time


    PLATFORM_CHOICES = [
        ('Teams', 'Teams'),
        ('Zoom', 'Zoom'),
        ('Google Meet', 'Google Meet'),
        ('In Person', 'In Person'),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    # Stores meeting platform (e.g. Zoom, Teams)
    message = models.TextField(blank=True)
    # Optional message field for additional details

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    # String representation of the model (useful for admin interface and debugging)
    