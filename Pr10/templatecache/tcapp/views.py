from django.shortcuts import render

# Create your views here.


def myhome(request):
    return render(request, "vcapp/home.html")
