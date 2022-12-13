from django.shortcuts import render, redirect
from .forms import Registrationform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# homepage

def homepage(request):
    return render(request, "login/home.html")


# user register

def user_register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            formdata = Registrationform(request.POST)
            if formdata.is_valid():
                formdata.save()
                messages.success(
                    request, "Register Successfully Please log in ")
                return redirect("/login/")

        else:
            formdata = Registrationform()
        return render(request, "login/enroll.html", {"form": formdata})
    else:
        return redirect("/profile/")

# user authenticate and login


def user_log(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            logdata = AuthenticationForm(request=request, data=request.POST)
            if logdata.is_valid():
                uname = logdata.cleaned_data["username"]
                ps = logdata.cleaned_data["password"]
                authdata = authenticate(username=uname, password=ps)
                if authdata is not None:
                    login(request, authdata)
                    messages.success(request, "login successfully")
                    return redirect("/profile/")
        else:
            logdata = AuthenticationForm()

        # return render(request, "login/user_login.html", {"form": logdata})
        return render(request, "login/user_login.html", {"form": logdata})
    else:
        return redirect("/profile/")

# show user profile


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, "login/profile.html", {"name": request.user})
    else:
        return redirect("/login/")


# user log out

def log_out(request):
    logout(request)
    return redirect("/login/")
