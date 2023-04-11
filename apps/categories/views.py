from django.shortcuts import render
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializers

# Create your views here.


class CategoryList(generics.ListAPIView):
    serializer_class=CategorySerializers
    queryset=Category.objects.all()
    
