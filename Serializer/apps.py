from django.apps import AppConfig


class SerializerConfig(AppConfig):
    name = 'Serializer'



    def ready(self):
       from . import signals
