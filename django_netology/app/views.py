from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .models import Product, Warehouse
from .serializers import ProductSerializer, WarehouseSerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
    pagination_class = PageNumberPagination

class WarehouseList(generics.ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product__name']
    pagination_class = PageNumberPagination
