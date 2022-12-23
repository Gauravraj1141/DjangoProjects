from django.shortcuts import render, HttpResponse

# Create your views here.

# here we generate a exception for checking our got_request_exception


def home(request):
    a = 10/0
    return HttpResponse("hey")
