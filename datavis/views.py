import json
from django.shortcuts import render
from core.models import Department, Team, TeamMember, Repository, Dependency


def dashboard(request):
    departments = Department.objects.all()
    teams = Team.objects.all()

    department_labels = []
    department_team_counts = []

    for department in departments:
        department_labels.append(department.name)
        department_team_counts.append(department.teams.count())

    team_labels = []
    team_member_counts = []
    team_repo_counts = []
    team_dependency_counts = []

    for team in teams:
        team_labels.append(team.name)
        team_member_counts.append(team.members.count())
        team_repo_counts.append(team.repositories.count())

        dependency_count = (
            Dependency.objects.filter(upstream_team=team).count()
            + Dependency.objects.filter(downstream_team=team).count()
        )
        team_dependency_counts.append(dependency_count)

    context = {
        "total_teams": Team.objects.count(),
        "total_departments": Department.objects.count(),
        "total_members": TeamMember.objects.count(),
        "total_repositories": Repository.objects.count(),
        "total_dependencies": Dependency.objects.count(),

        "department_labels": json.dumps(department_labels),
        "department_team_counts": json.dumps(department_team_counts),

        "team_labels": json.dumps(team_labels),
        "team_member_counts": json.dumps(team_member_counts),
        "team_repo_counts": json.dumps(team_repo_counts),
        "team_dependency_counts": json.dumps(team_dependency_counts),
    }

    return render(request, "datavis/dashboard.html", context)