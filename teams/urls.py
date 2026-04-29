from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('team/<int:id>/', views.team_detail,name = 'team_detail'),
]

