from django.shortcuts import render, redirect
from .models import Products, MenuCategory, Sales
from .forms import UsersForm


def index(request):
    context = {
        'title': 'Happy People | Main',
        'sales': Sales.objects.all(),
        'products': Products.objects.all(),
        'menu_category': MenuCategory.objects.all(),
        'forms': UsersForm()
    }
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/popup.html')
    else:
        return render(request, 'mainapp/index.html', context)
