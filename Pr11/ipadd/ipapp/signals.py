from django.contrib.auth.signals import user_logged_in

from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(user_logged_in, sender=User)
def userlogsignal(sender, request, user, **kwargs):
    print("------------------------")
    print("user logged in successfully ------------------------")
    userip = request.META.get('REMOTE_ADDR')
    # here we give ip in to session and it will unique for all particular user
    request.session["ip"] = userip
