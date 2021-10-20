from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=64, verbose_name='Модель телефона')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='', verbose_name='Изображение')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(blank=True, unique=True, verbose_name='URL')

    def __str__(self):
        return f'{self.id}:{self.name}'
