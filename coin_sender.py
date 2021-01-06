import json
import requests
import websockets

import random
import asyncio

from django.conf import settings
import coinwatch.settings as app_settings
settings.configure(INSTALLED_APPS=app_settings.INSTALLED_APPS,DATABASES=app_settings.DATABASES)
import django
django.setup()

from watch.models import CoinRate

from asgiref.sync import sync_to_async

@sync_to_async
def add_coin_rate_to_model(btc, eth):
    c = CoinRate(btc=float(btc), eth=float(eth))
    c.save()

# run a check every minute
delay = 60

async def main():
    while True:
        uri = "ws://localhost:8000"
        async with websockets.connect(uri) as websocket:
            btc_req = requests.get("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
            eth_req = requests.get("https://api.coinbase.com/v2/exchange-rates?currency=ETH")

            if btc_req.status_code == 200 and eth_req.status_code == 200:
                btc_data = btc_req.json()
                eth_data = eth_req.json()

                btc_value = btc_data['data']['rates']['USD']
                eth_value = eth_data['data']['rates']['USD']
                await websocket.send(json.dumps({
                    'BTC': btc_value,
                    'ETH': eth_value
                }))
                await add_coin_rate_to_model(btc_value, eth_value)

        await asyncio.sleep(delay)

asyncio.run(main())
