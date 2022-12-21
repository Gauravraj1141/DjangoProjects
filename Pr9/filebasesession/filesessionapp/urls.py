from django.urls import path
from . import views

urlpatterns = [
    path("", views.setsession),
    path("get", views.getsession, name="get"),
    path("del", views.delsession, name="del"),
]
