from django.shortcuts import render
from .models import CoinRate
import json

def index(request):
    latest_rates = CoinRate.objects.order_by('-time')[:60]
    times = list(map(lambda x: x.time.strftime("%H:%M:%S"), latest_rates))
    btc = list(map(lambda x: float(x.btc), latest_rates))
    eth = list(map(lambda x: float(x.eth), latest_rates))

    context = {
        "times": json.dumps(times),
        "btc": json.dumps(btc),
        "eth": json.dumps(eth)
    }
    return render(request, 'watch/index.html', context)
