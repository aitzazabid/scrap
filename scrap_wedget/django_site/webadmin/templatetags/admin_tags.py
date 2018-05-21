from django import template
from client.models import CurrencyGraph_values
register = template.Library()

import random
import json
from django.utils.safestring import mark_safe


@register.filter()
def graph_values(name):

    name = name
    list = []
    for i in range(0,7):
        r =  random.randint(1, 9)
        list.append(r)
    # return mark_safe(json.dumps(list))

    return list

    # CGV = CurrencyGraph_values.objects.filter(is_removed=False,name=name)
    # list = []
    # for values in CGV:
    #     list.append(float(values.price))

