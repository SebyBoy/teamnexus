# Sebastian Young - w2082018 - Student 6
import json
# used to convert Python data into JSON format

from django.shortcuts import render
# used to render HTML templates

from core.models import Department, Team, TeamMember, Repository, Dependency
# imports models from database


def dashboard(request):
# view function for dashboard page

    departments = Department.objects.all()
    # gets all departments

    teams = Team.objects.all()
    # gets all teams

    department_labels = []
    # list for department names

    department_team_counts = []
    # list for team counts per department

    for department in departments:
    # loops through each department

        department_labels.append(department.name)
        # adds department name to list

        department_team_counts.append(department.teams.count())
        # counts teams in that department

    team_labels = []
    # list for team names

    team_member_counts = []
    # list for number of members per team

    team_repo_counts = []
    # list for repos per team

    team_dependency_counts = []
    # list for dependencies per team

    for team in teams:
    # loops through each team

        team_labels.append(team.name)
        # adds team name

        team_member_counts.append(team.members.count())
        # counts members in team

        team_repo_counts.append(team.repositories.count())
        # counts repos in team

        dependency_count = (
            Dependency.objects.filter(upstream_team=team).count()
            + Dependency.objects.filter(downstream_team=team).count()
        )
        # counts dependencies related to team

        team_dependency_counts.append(dependency_count)
        # adds dependency count

    context = {
    # data passed to template

        "total_teams": Team.objects.count(),
        # total number of teams

        "total_departments": Department.objects.count(),
        # total departments

        "total_members": TeamMember.objects.count(),
        # total members

        "total_repositories": Repository.objects.count(),
        # total repos

        "total_dependencies": Dependency.objects.count(),
        # total dependencies

        "department_labels": json.dumps(department_labels),
        # converts department names to JSON

        "department_team_counts": json.dumps(department_team_counts),
        # converts department team counts to JSON

        "team_labels": json.dumps(team_labels),
        # converts team names to JSON

        "team_member_counts": json.dumps(team_member_counts),
        # converts member counts to JSON

        "team_repo_counts": json.dumps(team_repo_counts),
        # converts repo counts to JSON

        "team_dependency_counts": json.dumps(team_dependency_counts),
        # converts dependency counts to JSON
    }

    return render(request, "datavis/dashboard.html", context)
    # renders dashboard template with data
