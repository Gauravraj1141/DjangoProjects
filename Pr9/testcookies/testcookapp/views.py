from django.shortcuts import render

# Create your views here.


def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, 'ssapp/settestcookies.html')


def checktestcookie(request):
    status = request.session.test_cookie_worked()
    return render(request, 'ssapp/checktestcookies.html', {"status": status})


def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request, 'ssapp/deltestcookies.html')
