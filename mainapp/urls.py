from django.urls import path

from .views import ProductsListView

app_name = 'mainapp'

urlpatterns = [
    path('', ProductsListView.as_view(), name='products'),
    path('<int:pk>/', ProductsListView.as_view(), name='product'),
    path('page/<int:page>/', ProductsListView.as_view(), name='page'),
]
