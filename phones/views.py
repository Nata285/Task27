from audioop import reverse

from django.http import HttpResponse
from django.shortcuts import render

from phones.models import Phone

SORT_MAP = {
    'name': 'name',
    'max_price': '-price',
    'min_price': 'price',
}

def show_catalog(request):
    template = 'catalog.html'
    phone_catalog=Phone.objects.all()
    sort = request.GET.get('sort')
    if sort:
        phone_catalog = phone_catalog.order_by(SORT_MAP[sort])


    context = {'phone_catalog':phone_catalog}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    info=Phone.objects.all()
    phone_info=info.filter(slug = slug)
    context = {'phone_info': phone_info}

    return render(request, template, context)

