from django.shortcuts import render
from django.views.generic import ListView

from .models import Product, ProductCategory


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


class ProductsListView(ListView):
    paginate_by = 3
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'categories': ProductCategory.objects.all()})
        return context

    def get_queryset(self):
        try:
            return Product.objects.filter(category=self.kwargs['pk']).order_by('name')
        except:
            return Product.objects.all().order_by('name')
