import json
import requests
import websockets

import random
import asyncio

async def main():
    while True:
        uri = "ws://localhost:8000"
        async with websockets.connect(uri) as websocket:
            btc_req = requests.get("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
            eth_req = requests.get("https://api.coinbase.com/v2/exchange-rates?currency=ETH")

            if btc_req.status_code == 200 and eth_req.status_code == 200:
                btc_data = btc_req.json()
                eth_data = eth_req.json()
                await websocket.send(json.dumps({
                    'BTC': btc_data['data']['rates']['USD'],
                    'ETH': eth_data['data']['rates']['USD']
                }))
        await asyncio.sleep(10)

asyncio.run(main())
