from django.apps import AppConfig


class EchoConfig(AppConfig):
    name = 'Echo'
    verbose_name = "IQ Media Device Live Location"

    def ready(self):
        from . import signals
