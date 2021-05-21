from django.urls import path

from .views import products

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='products'),
    path('<int:category_id>/', products, name='product'),
    path('page/<int:page>/', products, name='page'),
]
