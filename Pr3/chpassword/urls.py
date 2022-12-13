from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.homepage),
    path("register", views.user_register, name="register"),
    path("login/", views.user_log, name="mylog"),
    path("profile/", views.user_profile, name="profile"),
    path("logout/", views.log_out, name="logout"),
    path("passwordch/", views.change_pass, name="passwordch"),
    path("passwordch1/", views.change_pass1, name="passwordch1"),
]
