from django.contrib import admin
from .models import Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_display_links = ('name', 'price')
    fields = ('name', 'category', ('price', 'quantity'), 'short_desc', 'description', 'image')
    ordering = ('price',)
    search_fields = ('name',)
