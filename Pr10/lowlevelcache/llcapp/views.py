from django.shortcuts import render

# here we need to import cache
from django.core.cache import cache

'''
def home(request):
    # here we can set and get cache and we give a default value in get 
    mydata = cache.get("name", "none")
    if mydata == "none":
        cache.set("name", "Rajput Gaurav", 30)
        mydata = cache.get("name")

    return render(request, "enroll/index.html", {"data": mydata})


'''

'''
def home(request):
    # here we give version 2 so in table it will show 
    # get or set means if it present in cache table then get it otherwise set it and then get it 
    gsdata = cache.get_or_set("village", "kalyanpur", 30, version=2)
    return render(request, "enroll/index.html", {"data": gsdata})
'''

'''
def home(request):
    # we can give same name cache data again with diff version
    gsdata = cache.get_or_set("village", "virampur", 30, version=3)
    return render(request, "enroll/index.html", {"data": gsdata})
'''

'''
def home(request):
    # if we have data in key and value means dict
    mydata = {"name": "gaurav Rajput", "profession": "sr er"}
    cache.set_many(mydata, 40)
    rsdata = cache.get_many(mydata)
    return render(request, "enroll/index.html", {"dict": rsdata})
'''


# if we want to delete any cache data with key name
'''
def home(request):
    cache.delete("name")

    return render(request, "enroll/index.html")

'''

'''
def home(request):
    # here we set roll no now we decrease and increase this roll no by decr and incr
    cache.set("rollno", 23, 400)

    return render(request, "enroll/index.html")'''


def home(request):
    # here we set roll no for 400 sec and we decrease this value 2 no roll no = 23 now value is 21
    # dr = cache.decr("rollno", delta=2)
    dr1 = cache.incr("rollno", delta=2)

    return render(request, "enroll/index.html", {"data": dr1})
