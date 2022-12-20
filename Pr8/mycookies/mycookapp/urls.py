
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.setcook, name="setcook"),
    path("get", views.getcook, name="get"),
    path("del", views.delcook, name="del"),
]
