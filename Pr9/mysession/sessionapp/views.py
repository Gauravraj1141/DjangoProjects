from django.shortcuts import render

# Create your views here.


def setsession(request):
    request.session["name"] = "Gaurav Rajput"
    request.session["Profession"] = "Software Engineer"

    # here we can set expiry of our session here 10 means in 10 sec
    request.session.set_expiry(10)

    # if we give here 0 then it will expire when browser will be close
    # request.session.set_expiry(0)

    return render(request, "ssapp/setsession.html")


def getsession(request):
    # name = request.session["name"]
    # if we need all data from session then we need to write it
    Sdata = request.session

    # it is only for keys
    keys = request.session.keys()

    # it is for key and value both we can get all key and value also :
    items = request.session.items()

    # it is for set value if value is not present in the session data then set the value otherwise get the value and we give default if value is not in session then it will return default value and set this default in the session data
    myage = request.session.setdefault("Age", "22")

    # it is for session cookies age
    session_cookies_age = request.session.get_session_cookie_age()
    session_expiry_age = request.session.get_expiry_age()
    session_cookies_date = request.session.get_expiry_date()
    session_expiry_atbrowserclose = request.session.get_expire_at_browser_close()
    mylm = {"session_expiry_age": session_expiry_age, "session_cookies_age": session_cookies_age,
            "session_cookies_date": session_cookies_date, "session_expiry_atbrowserclose": session_expiry_atbrowserclose}

    return render(request, "ssapp/getsession.html", {"name": Sdata, "key": keys, 'items': items, "myage": myage, "sometimedata": mylm})


def delsession(request):

    # it is delete all the session key data and all
    request.session.flush()
    # we should use this clear_expired because when our session will expire in 10 sec then in our database data will not delete so when we use it then data will clear.
    request.session.clear_expired()

    # if "name" and "Profession" in request.session:
    #     # it is for delete only session data
    #     del request.session['Profession']
    #     del request.session['name']

    return render(request, "ssapp/delsession.html")
