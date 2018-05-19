from django import template
from django.template.defaultfilters import floatformat
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


@register.filter()
def currency(amount):
    return '$ %s' % intcomma(floatformat(amount, 2))
