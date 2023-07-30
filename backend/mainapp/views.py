from django.shortcuts import render
from .models import Menu, MenuCategory


def index(requests):
    context = {
        'title': 'Happy People | Main',
        'menu': Menu.objects.all(),
        'menu_category': MenuCategory.objects.all()
    }
    return render(requests, 'mainapp/index.html', context)
