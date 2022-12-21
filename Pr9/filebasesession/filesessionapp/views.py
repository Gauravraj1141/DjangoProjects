from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def setsession(request):
    request.session["Name"] = "Gaurav Rajput"

    return render(request, "ssapp/setsession.html")


def getsession(request):
    sessiondata = request.session["Name"]
    return render(request, "ssapp/getsession.html", {"mydata": sessiondata})


def delsession(request):

    # it is delete all the session key data and all
    request.session.flush()
    # we should use this clear_expired because when our session will expire in 10 sec then in our database data will not delete so when we use it then data will clear.
    request.session.clear_expired()

    return render(request, "ssapp/delsession.html")
