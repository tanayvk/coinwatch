from django.db import models

class CoinRate(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    btc = models.DecimalField(max_digits=8, decimal_places=3)
    eth = models.DecimalField(max_digits=8, decimal_places=3)
