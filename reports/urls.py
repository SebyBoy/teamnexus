from django.urls import path
from .views import reports_page, export_teams_csv

urlpatterns = [
    path('', reports_page, name='reports'),
    path('export/', export_teams_csv, name='export_csv'),
]