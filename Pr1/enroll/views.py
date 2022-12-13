from django.shortcuts import render

# we import here usercreationform which show on our template it is readymade
# from django.contrib.auth.forms import UserCreationForm
from .forms import Custom_signupform
from django.contrib import messages
# Create your views here.


def sign_up(request):
    if request.method == "POST":
        formdata = Custom_signupform(request.POST)
        if formdata.is_valid():
            formdata.save()
            # we give msg when form will submit successfully then it will show
            messages.success(request, "Yor have been successfully registered")

    else:
        formdata = Custom_signupform()
    return render(request, "enroll/signup.html", {"form": formdata})
