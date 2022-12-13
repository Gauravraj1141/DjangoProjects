from django.shortcuts import render, redirect
from .forms import Registrationform
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages


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


# we change our password with old password
def change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            passdata = PasswordChangeForm(user=request.user, data=request.POST)
            if passdata.is_valid():
                passdata.save()
                messages.success(
                    request, 'Your password have been successfully updated !!')
                print(passdata.data, passdata.user)
                update_session_auth_hash(request, passdata.user)

                return redirect("/profile/")
        else:
            passdata = PasswordChangeForm(user=request.user)
        return render(request, "login/passwordchange.html", {"form": passdata})

    else:
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
                print(passdata.data, passdata.user)
                # we use this when we update password then seesion was expired so we didn't go to profile so we update session again and we use here agian login(user) it works
                update_session_auth_hash(request, passdata.user)

                return redirect("/profile/")
        else:
            passdata = SetPasswordForm(user=request.user)
        return render(request, "login/passwordchange1.html", {"form": passdata})

    else:
        return redirect("/login/")
