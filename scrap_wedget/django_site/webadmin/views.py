from django.shortcuts import render
from client.models import CapWedget
from client import table_dict

TEMPLATES = 'webadmin/%s.html'


def home(request):
    table_data=[]
    CW = CapWedget.objects.filter(is_removed=False).order_by('id')
    for rows in CW:
        table_data.append(table_dict(rows))
    return render(request, TEMPLATES % 'widget', {
        'table_data':table_data
    })


