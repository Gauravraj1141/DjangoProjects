from django.shortcuts import render, HttpResponse
from . import signals
# Create your views here.


def home(request):
    signals.notification.send(
        sender=None, request=request, user=["Gaurav", "rajput"])

    return HttpResponse("hey it is for testing of our custom signals ")
