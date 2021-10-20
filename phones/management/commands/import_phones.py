import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for line in phones:
            phone=Phone()
            self.name = line[1]
            self.image = line[2]
            self.price = line[3]
            self.release_date=line[4]
            self.lte_exists=line[5]
            phone.save()
            


