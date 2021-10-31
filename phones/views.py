from audioop import reverse

from django.http import HttpResponse
from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phone_catalog=Phone.objects.all()
    if request.GET.get('sort') == 'min_price':
        phone_catalog = Phone.objects.all().order_by('price')
    elif request.GET.get('sort') == 'max_price':
        phone_catalog = Phone.objects.all().order_by('-price')
    else:
        # request.GET.get('sort') == 'name':
        phone_catalog = Phone.objects.all().order_by('name')

    context = {'phone_catalog':phone_catalog}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'


    context = {}
    return render(request, template, context)

