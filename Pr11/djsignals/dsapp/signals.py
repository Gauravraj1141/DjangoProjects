from django.dispatch import receiver

from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

from django.contrib.auth.models import User


# here we work on models signals
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_delete, post_save, pre_migrate, post_migrate

# here we work on request signals

from django.core.signals import request_started, request_finished, got_request_exception


# migrate signals


@receiver(pre_migrate)
def premigrate_signal(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("-----------------------")
    print("Pre Migrate ..")
    print("sender", sender)
    print("app_config", app_config)
    print("verbosity", verbosity)
    print("interactive", interactive)
    print("using", using)
    print("plan", plan)
    print("apps", apps)
    print(f"kwargs : {kwargs}")


@receiver(post_migrate)
def after_migrate_models(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("-----------------------")
    print("post Migrate ..")
    print("sender", sender)
    print("app_config", app_config)
    print("verbosity", verbosity)
    print("interactive", interactive)
    print("using", using)
    print("plan", plan)
    print("apps", apps)
    print(f"kwargs : {kwargs}")


# request signals


@receiver(request_started)
def request_started_signals(sender, environ,  **kwargs):
    print("-----------------------")
    print("Reqest started signals")
    print("environ", environ)
    print("sender", sender)
    print(f"kwargs : {kwargs}")


@receiver(request_finished)
def request_finished_signals(sender,   **kwargs):
    print("-----------------------")
    print("Reqest finished signals")
    print("sender", sender)
    print(f"kwargs : {kwargs}")


@receiver(got_request_exception)
def request_exeption_signals(sender, request,  **kwargs):
    print("-----------------------")
    print("Reqest exception signals")
    print("request", request)
    print("sender", sender)
    print(f"kwargs : {kwargs}")


# Models signals

'''
@receiver(pre_init, sender=User)
def pre_init_singal(sender,  **kwargs):
    print("-----------------------")
    print("Pre in it signal")
    kwargs['name'] = kwargs.get('name', 'Default Name')
    print(kwargs["name"])
    print("sender", sender)
    print(f"kwargs : {kwargs}")


@receiver(post_init, sender=User)
def Post_init_signal(sender,  **kwargs):
    print("-----------------------")
    print("POst in it signal")
    kwargs['name'] = kwargs.get('name', 'Default Name')
    print(kwargs["name"])
    print("sender", sender)
    print(f"kwargs : {kwargs}")
'''


@receiver(pre_delete, sender=User)
def At_beggining_delete(sender, instance, **kwargs):
    print("-----------------------")
    print("Pre delete ..")
    print("sender", sender)
    print("instance", instance)
    print(f"kwargs : {kwargs}")


@receiver(post_delete, sender=User)
def At_Post_delete(sender, instance, **kwargs):
    print("-----------------------")
    print("Post delete ..")
    print("sender", sender)
    print("instance", instance)
    print(f"kwargs : {kwargs}")


@receiver(pre_save, sender=User)
def At_beggining_save(sender, instance, **kwargs):
    print("-----------------------")
    print("Pre save signal ..")
    print("sender", sender)
    print("instance", instance)
    print(f"kwargs : {kwargs}")


@receiver(post_save, sender=User)
def post_save_signals(sender, instance, created, **kwargs):
    if created:
        print("-----------------------")
        print("Post save signal ..")
        print("New User created")
        print("sender", sender)
        print("instance", instance)
        print(f"kwargs : {kwargs}")
    else:
        print("-----------------------")
        print("Post save signal ..")
        print("Update User ")
        print("sender", sender)
        print("instance", instance)
        print(f"kwargs : {kwargs}")


# auth signals

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("-----------------------")
    print("Logged-in Signal ... run-intro")
    print("sender", sender)
    print("request", request)
    print("User", user)
    print(f"kwargs : {kwargs}")

# here we use connect method but we can use decorator which we use in it also but mostly we use this decorator for connect  sender to this signal
# user_logged_in.connect(login_success, sender=User)


@receiver(user_logged_out, sender=User)
def logout_signal(sender, request, user, **kwargs):
    print("-----------------------")
    print("Logged-Out Signal ... run-outro")
    print("sender", sender)
    print("request", request)
    print("User", user)
    print(f"kwargs : {kwargs}")


@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("-----------------------")
    print("Login Failed ..")
    print("sender", sender)
    print("request", request)
    print("credentials", credentials)
    print(f"kwargs : {kwargs}")
