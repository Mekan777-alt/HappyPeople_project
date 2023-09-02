from django.shortcuts import render
from .models import Products, MenuCategory


def index(requests):
    context = {
        'title': 'Happy People | Main',
        'products': Products.objects.all(),
        'menu_category': MenuCategory.objects.all(),

    }
    return render(requests, 'mainapp/index.html', context)
