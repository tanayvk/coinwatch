from django.shortcuts import render
from .models import CoinRate
import json
import datetime

def index(request):
    latest_rates = CoinRate.objects.order_by('-time')[:60]
    times = list(map(lambda x: convertTime(x.time), latest_rates))
    btc = list(map(lambda x: float(x.btc), latest_rates))
    eth = list(map(lambda x: float(x.eth), latest_rates))

    times.reverse()
    btc.reverse()
    eth.reverse()

    context = {
        "times": json.dumps(times),
        "btc": json.dumps(btc),
        "eth": json.dumps(eth)
    }
    return render(request, 'watch/index.html', context)

def convertTime(time):
    return time.strftime("%c %z")
