from django.apps import AppConfig


class DsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dsapp'

    def ready(self):
        # import signals
        import dsapp.signals
