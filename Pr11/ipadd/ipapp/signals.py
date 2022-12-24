from django.contrib.auth.signals import user_logged_in

from django.dispatch import receiver
from django.contrib.auth.models import User

from django.core.cache import cache


@receiver(user_logged_in, sender=User)
def userlogsignal(sender, request, user, **kwargs):
    print("------------------------")
    print("user logged in successfully ------------------------")
    userip = request.META.get('REMOTE_ADDR')
    # here we give ip in to session and it will unique for all particular user
    request.session["ip"] = userip

    # now we count user login how many time user login in today so we count it by cache and it expire daily user.pk = userid so all user's version will be diff
    count = cache.get("counter", 0, version=user.pk)
    print(count, user.pk)
    newcount = count + 1
    cache.set("counter", newcount, 60*60*24, version=user.pk)
