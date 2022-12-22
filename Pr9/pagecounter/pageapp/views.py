from django.shortcuts import render

# Create your views here.


def home(request):
    ct = request.session.get("count", 0)
    pgcount = ct + 1
    request.session["count"] = pgcount
    return render(request, "pageapp/index.html", {"c": ct})
