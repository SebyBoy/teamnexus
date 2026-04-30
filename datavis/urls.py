# Sebastian Young - w2082018 - Student 6
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]
# defines URL route linking homepage to dashboard view
