from django.apps import AppConfig


class IpappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ipapp'

    def ready(self):
        import ipapp.signals
