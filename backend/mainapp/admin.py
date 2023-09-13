from django.contrib import admin
from .models import MenuCategory, Products, Sales, Users


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'category')


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price')


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')

