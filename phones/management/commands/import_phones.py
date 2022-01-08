import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))


        for line in phones:
            try:

                name = line['name']
                image = line['image']
                price = line['price']
                release_date=line['release_date']
                lte_exists=line['lte_exists']
                phone = Phone.objects.create(name=name,slug=slugify(name),
                    image=image,
                    price=price,
                    release_date=release_date,
                    lte_exists=lte_exists)

            except:
                continue






