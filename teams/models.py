

# Create your models here.
from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)
    department_head = models.CharField(max_length=100, blank=True, null=True)
    team_leader = models.CharField(max_length=100, blank=True, null=True)
    development_focus_area = models.TextField(blank=True, null=True)
    key_skills_technologies = models.TextField(blank=True, null=True)
    upstream_dependencies = models.TextField(blank=True, null=True)
    downstream_dependencies = models.TextField(blank=True, null=True)
    dependency_type = models.TextField(blank=True, null=True)
    code_repository = models.URLField(blank=True, null=True)
    jira_project_name = models.CharField(max_length=100, blank=True, null=True)
    jira_board_link = models.URLField(blank=True, null=True)
    team_wiki = models.URLField(blank=True, null=True)
    

    #description = models.CharField(max_length=100)
    #skills = models.CharField(max_length = 225,help_text = "comma separated skills")
    #dependencies = models.ManyToManyField('self', blank = True)
    #email = models.EmailField(blank = True)

    def __str__(self):
        return self.name