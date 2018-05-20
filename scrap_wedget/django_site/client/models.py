from django.db import models


class CapWedget(models.Model):
    rank = models.IntegerField(null=True)
    name = models.TextField(null=True)
    market_cap = models.TextField(null=True)
    price = models.TextField(null=True)
    volume_24 = models.TextField(null=True)
    circulatory_supply = models.TextField(null=True)
    change = models.TextField(null=True)
    symbol = models.TextField(null=True)

    available_supply = models.TextField(null=True)
    total_supply = models.TextField(null=True)
    max_supply = models.TextField(null=True)
    percent_change_1h = models.TextField(null=True)
    percent_change_24h =  models.TextField(null=True)
    percent_change_7d = models.TextField(null=True)
    last_update = models.TextField(null=True)
    is_removed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True)


class CurrencyGraph_values(models.Model):
    rank = models.IntegerField(null=True)
    name = models.TextField(null=True)
    market_cap = models.TextField(null=True)
    price = models.TextField(null=True)
    volume_24 = models.TextField(null=True)
    circulatory_supply = models.TextField(null=True)
    change = models.TextField(null=True)
    symbol = models.TextField(null=True)

    available_supply = models.TextField(null=True)
    total_supply = models.TextField(null=True)
    max_supply = models.TextField(null=True)
    percent_change_1h = models.TextField(null=True)
    percent_change_24h = models.TextField(null=True)
    percent_change_7d = models.TextField(null=True)
    last_update = models.TextField(null=True)
    is_removed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True)
