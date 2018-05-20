from django.shortcuts import render
from client.models import CapWedget
from client import currency_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


TEMPLATES = 'webadmin/%s.html'


def home(request):

    page = request.GET.get('page', 1)
    search_string = request.GET.get('search_string')
    if search_string:
        CW = CapWedget.objects.filter(is_removed=False,name__icontains=search_string).order_by('rank')
    else:
        CW = CapWedget.objects.filter(is_removed=False).order_by('rank')

    paginator = Paginator(CW, 30)
    try:
        table_data = paginator.page(page)
    except PageNotAnInteger:
        table_data = paginator.page(1)
    except EmptyPage:
        table_data = paginator.page(paginator.num_pages)

    return render(request, TEMPLATES % 'widget', {
        'table_data': table_data
    })


def currency_detail(request):

    currency = request.GET.get('currency')

    CW = CapWedget.objects.get(is_removed=False,rank=currency)

    currency_detail  = currency_dict(CW)

    return render(request, TEMPLATES % 'currency_detail', {
        'currency_detail': currency_detail
    })




