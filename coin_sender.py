import json
import requests
import websockets

import random
import asyncio
import sys
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'coinwatch.settings'
import django
django.setup()

from watch.models import CoinRate

from asgiref.sync import sync_to_async

@sync_to_async
def add_coin_rate_to_model(btc, eth):
    c = CoinRate(btc=float(btc), eth=float(eth))
    c.save()

    return c.time

# run a check every minute
delay = 60

port = 8000
if len(sys.argv) > 1:
    port = sys.argv[1]

async def main():
    while True:
        uri = "ws://localhost:" + str(port)
        async with websockets.connect(uri) as websocket:
            btc_req = requests.get("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
            eth_req = requests.get("https://api.coinbase.com/v2/exchange-rates?currency=ETH")

            if btc_req.status_code == 200 and eth_req.status_code == 200:
                btc_data = btc_req.json()
                eth_data = eth_req.json()

                btc_value = btc_data['data']['rates']['USD']
                eth_value = eth_data['data']['rates']['USD']
                time = await add_coin_rate_to_model(btc_value, eth_value)

                await websocket.send(json.dumps({
                    'time': time.strftime("%c %z"),
                    'BTC': btc_value,
                    'ETH': eth_value
                }))
        await asyncio.sleep(delay)

asyncio.run(main())
