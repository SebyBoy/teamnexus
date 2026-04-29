from django.db import models

# -------------------
# User
# -------------------
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# -------------------
# Department
# -------------------
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.department_name


# -------------------
# Team
# -------------------
class Team(models.Model):
    team_name = models.CharField(max_length=100)
    description = models.TextField()
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name


# -------------------
# TeamMember
# -------------------
class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# -------------------
# Repository
# -------------------
class Repository(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    repository_name = models.CharField(max_length=100)
    platform = models.CharField(max_length=50)


# -------------------
# ContactChannel
# -------------------
class ContactChannel(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    value = models.CharField(max_length=255)


# -------------------
# Dependency
# -------------------
class Dependency(models.Model):
    from_team = models.ForeignKey(Team, related_name='dependencies', on_delete=models.CASCADE)
    to_team = models.ForeignKey(Team, related_name='dependents', on_delete=models.CASCADE)


# -------------------
# Message
# -------------------
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


# -------------------
# Meeting
# -------------------
class Meeting(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    organiser = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()