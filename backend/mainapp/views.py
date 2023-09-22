from django.shortcuts import render
from django.http import JsonResponse
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
    else:
        return render(request, 'mainapp/index.html', context)


def booking(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            errors = form.errors
            return JsonResponse({"success": False, "errors": errors})
    else:
        form = UsersForm()
        return render(request, 'mainapp/reserved.html', {"form": form})
