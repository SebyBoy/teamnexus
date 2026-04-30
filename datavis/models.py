from django.db import models
# imports Django models module

class Department(models.Model):
# model for departments

    name = models.CharField(max_length=100)
    # stores department name

    head = models.CharField(max_length=100, blank=True)
    # stores department head (optional)

    def __str__(self):
        return self.name
    # returns name when object is printed


class Manager(models.Model):              
# model for managers

    name = models.CharField(max_length=100)
    # stores manager name

    email = models.EmailField(blank=True)
    # stores manager email (optional)

    def __str__(self):
        return self.name
    # returns name when printed


class Team(models.Model):
# model for teams

    name = models.CharField(max_length=100)
    # stores team name

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="teams")
    # links team to a department

    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, blank=True, related_name="teams")
    # links team to a manager (optional)

    description = models.TextField(blank=True)
    # stores team description

    def __str__(self):
        return self.name
    # returns team name


class TeamMember(models.Model):
# model for team members

    name = models.CharField(max_length=100)
    # stores member name

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="members")
    # links member to a team

    def __str__(self):
        return self.name
    # returns member name


class Repository(models.Model):
# model for repositories

    name = models.CharField(max_length=100)
    # stores repo name

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="repositories")
    # links repo to a team

    url = models.URLField(blank=True)
    # stores repo link

    def __str__(self):
        return self.name
    # returns repo name


class Dependency(models.Model):
# model for team dependencies

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="dependencies")
    # team that depends on another

    depends_on = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="dependent_teams")
    # team being depended on

    def __str__(self):
        return f"{self.team.name} depends on {self.depends_on.name}"
    # returns readable dependency info
