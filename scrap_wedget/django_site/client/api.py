from bs4 import BeautifulSoup
import urllib2
import requests
from client.rest_decorators import public_rest_call
from util.utility_function import *
from client.models import CapWedget,CurrencyGraph_values
import json

@public_rest_call
def coincap(request):
    try:
        response = requests.get('https://api.coinmarketcap.com/v1/ticker/?start=0&limit=1000')
        result = json.loads(response.text)
        for items in result:
            rank = items['rank']
            name = items['name']
            market_cap =items['market_cap_usd']
            price =items['price_usd']
            volume_24 =items['24h_volume_usd']
            circulatory_supply =items['available_supply']
            symbol = items['symbol']
            change =items['percent_change_24h']

            available_supply = items['available_supply']
            total_supply = items['total_supply']
            max_supply = items['max_supply']
            percent_change_1h = items['percent_change_1h']
            percent_change_24h = items['percent_change_24h']
            percent_change_7d = items['percent_change_7d']
            last_update = items['last_updated']

            cap_weg, created =  CapWedget.objects.get_or_create( name=name)
            cap_weg.rank = rank
            cap_weg.market_cap = market_cap
            cap_weg.price = price
            cap_weg.volume_24 = volume_24
            cap_weg.circulatory_supply = circulatory_supply
            cap_weg.change = change
            cap_weg.available_supply = available_supply
            cap_weg.total_supply = total_supply
            cap_weg.max_supply = max_supply
            cap_weg.symbol = symbol
            cap_weg.percent_change_1h = percent_change_1h
            cap_weg.percent_change_24h = percent_change_24h
            cap_weg.percent_change_7d = percent_change_7d
            cap_weg.last_update = last_update
            cap_weg.save()

        return {'success': True
                }
    except Exception as  e:
        print("e",e)


@public_rest_call
def coin_graph_values(request):
    try:
        response = requests.get('https://api.coinmarketcap.com/v1/ticker/?start=0&limit=1000')
        result = json.loads(response.text)
        for items in result:
            rank = items['rank']
            name = items['name']
            market_cap =items['market_cap_usd']
            price =items['price_usd']
            volume_24 =items['24h_volume_usd']
            circulatory_supply =items['available_supply']
            symbol = items['symbol']
            change =items['percent_change_24h']

            available_supply = items['available_supply']
            total_supply = items['total_supply']
            max_supply = items['max_supply']
            percent_change_1h = items['percent_change_1h']
            percent_change_24h = items['percent_change_24h']
            percent_change_7d = items['percent_change_7d']
            last_update = items['last_updated']

            cap_weg=  CurrencyGraph_values.objects.create( name=name)
            cap_weg.rank = rank
            cap_weg.market_cap = market_cap
            cap_weg.price = price
            cap_weg.volume_24 = volume_24
            cap_weg.circulatory_supply = circulatory_supply
            cap_weg.change = change
            cap_weg.available_supply = available_supply
            cap_weg.total_supply = total_supply
            cap_weg.max_supply = max_supply
            cap_weg.symbol = symbol
            cap_weg.percent_change_1h = percent_change_1h
            cap_weg.percent_change_24h = percent_change_24h
            cap_weg.percent_change_7d = percent_change_7d
            cap_weg.last_update = last_update
            cap_weg.save()

        return {'success': True
                }
    except Exception as  e:
        print("e",e)