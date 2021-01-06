from django.conf.urls import url
from . import consumers

websocket_urlpatterns = [
    url('', consumers.CoinConsumer.as_asgi()),
]


