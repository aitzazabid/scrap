from django import template
from client.models import CurrencyGraph_values
register = template.Library()



@register.filter()
def graph_values(name):

    name = name

    CGV = CurrencyGraph_values.objects.filter(is_removed=False,name=name)
    list = []
    for values in CGV:
        list.append(float(values.price))
    return list
