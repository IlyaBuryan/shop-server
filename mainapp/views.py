from django.shortcuts import render
import json


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    with open('mainapp/fictures/products.json', 'r', encoding='utf-8') as file:
        products = json.load(file)

    context = {
        'title': 'GeekShop - catalog',
        'products': products,
    }
    return render(request, 'mainapp/products.html', context)
