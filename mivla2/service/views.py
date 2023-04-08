from django.shortcuts import render
from .parent import get_all, get


def main_page(request):
    return render(request, template_name='service/index.html')


def view_get_all(request):
    context = {"entities": get_all()}
    return render(request, template_name='service/catalog.html', context=context)

