from bs4 import BeautifulSoup
import urllib2
import requests
from client.rest_decorators import public_rest_call
from util.utility_function import *
from client.models import CapWedget


@public_rest_call
def coincap(request):
    try:
        response = requests.post('http://easyascrypto.com/exchange_rates.php')
        soup = BeautifulSoup(response.text, 'lxml')
        table_content = soup.find_all('table')
        table_content = table_content[0].find_all('tbody')
        for colum in table_content[0].find_all('tr'):
            columns = colum.find_all('td')
            rank = columns[0].get_text()
            name = columns[1].get_text()
            market_cap = columns[2].get_text()
            price = columns[3].get_text()
            volume_24 = columns[4].get_text()
            circulatory_supply = columns[5].get_text()
            change = columns[6].get_text()
            cap_weg, created =  CapWedget.objects.get_or_create( name=name)
            cap_weg.rank = rank
            cap_weg.market_cap = market_cap
            cap_weg.price = price
            cap_weg.volume_24 = volume_24
            cap_weg.circulatory_supply = circulatory_supply
            cap_weg.change = change
            cap_weg.save()

        return {'success': True
                }
    except Exception as  e:
        print("e",e)
