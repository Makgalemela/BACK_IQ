from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from Echo.consumers import NoseyConsumer
from django.conf.urls import url

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path('ws/', NoseyConsumer),
    ])
})