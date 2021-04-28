from django.shortcuts import render
from .models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()

    context = {
        'title': 'GeekShop - catalog',
        'products': products,
        'categories': categories
    }
    return render(request, 'mainapp/products.html', context)
