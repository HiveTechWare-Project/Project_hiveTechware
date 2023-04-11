from django.shortcuts import render
from django.db.models import query
from rest_framework import generics, serializers
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProductSerializer
from rest_framework import filters
from .models import Product
# Create your views here.


class ProductList(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends= [DjangoFilterBackend, filters.SearchFilter]
    filterset_feilds= ['type']
    search_feilds= ['name', 'description']