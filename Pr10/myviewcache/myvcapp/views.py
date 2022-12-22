from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

# we use here decorator for cache data and give time only 20 sec


@cache_page(20)
def home(request):
    return render(request, 'vcapp/home.html')


def contact(request):
    return render(request, 'vcapp/contact.html')
