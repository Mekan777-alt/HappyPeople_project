from django.shortcuts import render
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
    return render(request, 'mainapp/index.html', context)


# def orders(request):
#     if request.method == 'POST':
#         form = UsersForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'mainapp/index.html')
#     else:
#         form = UsersForm
#         return render(request, 'mainapp/index.html', {'form': form})
