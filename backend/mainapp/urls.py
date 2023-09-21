from django.urls import path
from .views import index, booking

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('booking/', booking, name='booking')
]
