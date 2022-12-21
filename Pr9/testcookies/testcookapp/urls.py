from django.urls import path
from . import views

urlpatterns = [
    path("", views.settestcookie),
    path("check", views.checktestcookie, name="check"),
    path("del", views.deltestcookie, name="del"),
]
