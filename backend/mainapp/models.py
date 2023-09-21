import datetime

import django.utils.timezone
from django.db import models


class MenuCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name='Категория')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Разновидность меню'
        verbose_name_plural = 'Разновидность меню'

    def __str__(self):
        return self.name


class Products(models.Model):
    name_product = models.CharField(max_length=64, verbose_name='Название продукта')
    description_product = models.TextField(verbose_name='Описание продукта')
    photo_product = models.ImageField(upload_to='product', null=True, blank=True, verbose_name='Фотография продукта')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена продукта')
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name_product} - {self.category}'


class Sales(models.Model):
    product_name = models.CharField(max_length=64, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание продукта')
    photo = models.ImageField(upload_to='sales_product', null=True, blank=True, verbose_name='Фотография продукта')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='Цена продукта')

    class Meta:
        verbose_name = 'Особое предложение'
        verbose_name_plural = 'Особое предложение'

    def __str__(self):
        return self.product_name


class Users(models.Model):
    name = models.CharField(max_length=64, verbose_name='Имя')
    phone_number = models.CharField(max_length=15, verbose_name='Телефон номер')
    people_number = models.PositiveIntegerField(verbose_name='Количество человек')
    date = models.CharField(max_length=15, verbose_name='Дата брони')
    time = models.CharField(max_length=5, verbose_name='Время брони')
    time_register = models.DateTimeField(default=django.utils.timezone.now, verbose_name='Когда пришла бронь')

    class Meta:
        verbose_name = 'Брони'
        verbose_name_plural = 'Брони'

    def __str__(self):
        return f"{self.name} - {self.phone_number}"
