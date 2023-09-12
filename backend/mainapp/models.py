from django.db import models


class MenuCategory(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Разновидность меню'
        verbose_name_plural = 'Разновидность меню'

    def __str__(self):
        return self.name


class Products(models.Model):
    name_product = models.CharField(max_length=64)
    description_product = models.TextField()
    photo_product = models.ImageField(upload_to='product', null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name_product} - {self.category}'


class Sales(models.Model):
    product_name = models.CharField(max_length=64)
    description = models.TextField()
    photo = models.ImageField(upload_to='sales_product', null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Особое предложение'
        verbose_name_plural = 'Особое предложение'

    def __str__(self):
        return self.product_name


class Users(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=20)
    phone_number = models.IntegerField(null=False, blank=False)
    people_number = models.PositiveIntegerField()
    date = models.CharField(max_length=15)
    time = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'Брони'
        verbose_name_plural = 'Брони'

    def __str__(self):
        return f"{self.name} - {self.phone_number}"
