from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.homepage),
    path("register", views.user_register, name="register"),
    path("login/", views.user_log, name="mylog"),
    path("profile/", views.user_profile, name="profile"),
    path("logout/", views.log_out, name="logout"),
    path("passwordch1/", views.change_pass1, name="passwordch1"),
    path("details/<int:id>/", views.user_details, name="details"),
]
