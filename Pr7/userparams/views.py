from django.shortcuts import render, redirect
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# we import from forms.py all our custom forms

from .forms import Registrationform, user_login_form
# homepage


def homepage(request):
    if request.user.is_authenticated:
        return redirect("/dashbord/")
    else:
        return render(request, "login/home.html")


# user register

def user_register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            formdata = Registrationform(request.POST)
            if formdata.is_valid():
                totaldata = formdata.save()
                # we get the viewers data from group model
                group = Group.objects.get(name="viewers")
                totaldata.groups.add(group)

                messages.success(
                    request, "Register Successfully ")
                return redirect("/login/")

        else:
            formdata = Registrationform()
        return render(request, "login/enroll.html", {"form": formdata})
    else:
        return redirect("/dashbord/")

# user authenticate and login


def user_log(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            logdata = user_login_form(request=request, data=request.POST)
            if logdata.is_valid():
                uname = logdata.cleaned_data["username"]
                ps = logdata.cleaned_data["password"]
                authdata = authenticate(username=uname, password=ps)
                if authdata is not None:
                    login(request, authdata)
                    messages.success(request, "login successfully")
                    return redirect("/dashbord/")
        else:
            logdata = user_login_form()

        # return render(request, "login/user_login.html", {"form": logdata})
        return render(request, "login/nlogin.html", {"form": logdata})
    else:
        return redirect("/dashbord/")


# show user profile


def user_dashbord(request):
    if request.user.is_authenticated:
        name = request.user

        return render(request, "login/profile.html", {"name": name})
    else:
        return redirect("/login/")


# user log out

def log_out(request):
    logout(request)
    return redirect("/login/")
