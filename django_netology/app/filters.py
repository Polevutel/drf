import django_filters
from .models import Product, Warehouse

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name', 'description']

class WarehouseFilter(django_filters.FilterSet):
    class Meta:
        model = Warehouse
        fields = ['product__name', 'cost']
