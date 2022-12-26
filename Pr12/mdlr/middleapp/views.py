from django.shortcuts import render, HttpResponse

from django.template.response import TemplateResponse

# Create your views here.


def home(request):
    print("hey it is views")
    return HttpResponse("hey it is views")


def execptiontest(request):
    a = 10/0
    return HttpResponse("hey it is my views with exception")


def processtemplate(request):
    context = {"name": "radha"}
    return TemplateResponse(request, 'middle/index.html', context)
