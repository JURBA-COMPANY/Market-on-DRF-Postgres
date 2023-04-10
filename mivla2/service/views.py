from django.shortcuts import render
from .parent import Service
from .models import *


def shop(request):
    product = Service()
    lister = product.get_all(Sofa, Wardrobe, Stol)
    context = {'items': lister}
    return render(request, 'service/catalog.html', context)
