import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CoinConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'coindata'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'process',
                'value': text_data,
            }
        )

        print ('>>>>', text_data)

    async def process(self,event):
        await self.send(text_data=event['value'])
