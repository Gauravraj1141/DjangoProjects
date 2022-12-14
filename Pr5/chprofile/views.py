from django.shortcuts import render, redirect
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages

# we import from forms.py all our custom forms

from .forms import Registrationform, user_login_form, user_profile_change, Admin_profile_view

# homepage


def homepage(request):
    if request.user.is_authenticated:
        return redirect("/profile/")
    else:
        return render(request, "login/home.html")


# user register

def user_register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            formdata = Registrationform(request.POST)
            if formdata.is_valid():
                formdata.save()
                messages.success(
                    request, "Register Successfully ")
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
            logdata = user_login_form(request=request, data=request.POST)
            if logdata.is_valid():
                uname = logdata.cleaned_data["username"]
                ps = logdata.cleaned_data["password"]
                authdata = authenticate(username=uname, password=ps)
                if authdata is not None:
                    login(request, authdata)
                    messages.success(request, "login successfully")
                    return redirect("/profile/")
        else:
            logdata = user_login_form()

        # return render(request, "login/user_login.html", {"form": logdata})
        return render(request, "login/nlogin.html", {"form": logdata})
    else:
        return redirect("/profile/")

# show user profile


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser:
                All_users_data = User.objects.all()
                formdata = Admin_profile_view(
                    request.POST, instance=request.user)

            else:
                All_users_data = None
                formdata = user_profile_change(
                    request.POST, instance=request.user)
            if formdata.is_valid():
                formdata.save()
                messages.success(request, "updated profile successfully!!")
        else:
            if request.user.is_superuser:
                All_users_data = User.objects.all()
                formdata = Admin_profile_view(instance=request.user)
            else:
                All_users_data = None
                formdata = user_profile_change(instance=request.user)
        return render(request, "login/profile.html", {"name": request.user, "fm": formdata, "userdata": All_users_data})
    else:
        return redirect("/login/")


# user log out

def log_out(request):
    logout(request)
    return redirect("/login/")


# we change our password without old password only newpassword

def change_pass1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # it will update password without enter old password
            passdata = SetPasswordForm(user=request.user, data=request.POST)
            if passdata.is_valid():
                passdata.save()
                messages.success(
                    request, 'Your password have been successfully updated !!')

                # we use this when we update password then seesion was expired so we didn't go to profile so we update session again and we use here agian login(user) it works
                update_session_auth_hash(request, passdata.user)

                return redirect("/profile/")
        else:
            passdata = SetPasswordForm(user=request.user)
        return render(request, "login/passwordchange1.html", {"form": passdata})

    else:
        return redirect("/login/")


# for showing user details these can see only admin bro

def user_details(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            userdata = User.objects.get(pk=id)
            detailsform = Admin_profile_view(request.POST, instance=userdata)
            if detailsform.is_valid():
                detailsform.save()
                messages.success(request, "details updated")
        else:
            userdata = User.objects.get(pk=id)
            detailsform = Admin_profile_view(instance=userdata)

        return render(request, "login/details.html", {"name": request.user, "fm": detailsform})
    else:
        return redirect("/login/")
