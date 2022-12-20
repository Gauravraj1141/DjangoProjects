from django.shortcuts import render
from datetime import datetime, timedelta


# it is for normal cookies


# when we set cookies so these expire when our browser will close and if we give time limit then it will delete that particular time period


# def setcook(request):
#     response = render(request, "mycook/setcook.html")
#     # if we want to set the user name in our cookies then we use this request.user.username and if user is not login then it will give annoymous user
#     # response.set_cookie("Name", request.user)

#     # so we give 2 days time for this cookie expiration
#     # response.set_cookie("Name", "Gaurav Rajput",
#     #                     expires=datetime.now+timedelta(days=2))
#     # here we give 1 minute means 60 sec
#     response.set_cookie("Name", "Gaurav Rajput",
#                         expires=60)
#     return response


# def getcook(request):
#     # getcookies = request.COOKIES['Name']
#     # here when we use get function then we give a default value in it
#     getcookies = request.COOKIES.get("Name", "User")
#     return render(request, "mycook/getcook.html", {"name": getcookies})


# def delcook(request):
#     response = render(request, "mycook/deletecook.html")
#     response.delete_cookie("Name")
#     return response


# it is for signed cookies

def setcook(request):
    response = render(request, "mycook/setcook.html")

    response.set_signed_cookie("Name", "Gaurav Rajput", salt="guru")
    return response

# here is we give right salt value then name will show otherwise defalt value will come user


def getcook(request):
    getcookies = request.get_signed_cookie("Name", "User", salt="guru")
    return render(request, "mycook/getcook.html", {"name": getcookies})


def delcook(request):
    response = render(request, "mycook/deletecook.html")
    response.delete_cookie("Name")
    return response
