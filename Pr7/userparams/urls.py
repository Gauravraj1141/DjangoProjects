from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.homepage),
    path("register", views.user_register, name="register"),
    path("login/", views.user_log, name="mylog"),
    path("dashbord/", views.user_dashbord, name="dashbord"),
    path("logout/", views.log_out, name="logout")
]
