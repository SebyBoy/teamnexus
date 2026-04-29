from django.shortcuts import render

def base(request):
    return render(request, "teams/base.html")

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from core.models import Team
from django.db.models import Q
from urllib.parse import urlencode


def team_list(request):
    teams = Team.objects.all()

    query = request.GET.get("q", "")
    department = request.GET.get("department", "")
    department_head = request.GET.get("department_head", "")
    sort = request.GET.get("sort", "az")

    if query:
        teams = teams.filter(
            Q(name__icontains=query)
            | Q(department__name__icontains=query)
            | Q(team_leader_name__icontains=query)
        )

    if department:
        teams = teams.filter(department__name=department)

    if department_head:
        teams = teams.filter(department_head=department_head)

    if sort == "za":
        teams = teams.order_by("-name")
    else:
        teams = teams.order_by("name")

    paginator = Paginator(teams, 5)
    page_number = request.GET.get("page")
    teams = paginator.get_page(page_number)

    params = request.GET.copy()
    params.pop("page", None)
    query_params = urlencode(params, doseq=True)

    return render(
        request,
        "teams/team_list.html",
        {
            "teams": teams,
            "query": query,
            "department": department,
            "department_head": department_head,
            "sort": sort,
            "query_params": query_params,
        },
    )


def team_detail(request, id):
    team = get_object_or_404(Team, id=id)

    return render(request, "teams/team_detail.html", {"team": team})