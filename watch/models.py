from django.db import models
from django.utils import timezone
from datetime import datetime

def current_time():
    return timezone.now()

class CoinRate(models.Model):
    time = models.DateTimeField(default=current_time)
    btc = models.DecimalField(max_digits=8, decimal_places=3)
    eth = models.DecimalField(max_digits=8, decimal_places=3)
