# schedule/urls.py
# blenda jashari - w19760609 
# student4
from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_page, name='schedule_page'),
]