from django.shortcuts import render
from core.models import Team, Department

def reports_page(request):
    department_id = request.GET.get('department')

    teams = Team.objects.all()

    if department_id:
        teams = teams.filter(department_id=department_id)

    departments = Department.objects.all()

    total_teams = teams.count()
    no_manager = teams.filter(manager__isnull=True)

    return render(request, 'reports.html', {
        'teams': teams,
        'departments': departments,
        'total_teams': total_teams,
        'no_manager': no_manager
    })


import csv
from django.http import HttpResponse
from core.models import Team


def export_teams_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="team_report.csv"'

    writer = csv.writer(response)
    writer.writerow(["Team", "Department", "Manager"])

    teams = Team.objects.select_related("department", "manager").all()

    for team in teams:
        if team.manager:
            manager_name = f"{team.manager.first_name} {team.manager.last_name}".strip()
            if not manager_name:
                manager_name = team.manager.username
        else:
            manager_name = "No Manager"

        writer.writerow([
            team.name,
            team.department.name if team.department else "No Department",
            manager_name,
        ])

    return response