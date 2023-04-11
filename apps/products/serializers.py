from .models import Product
from rest_framework import serializers
from apps.categories.serializers import CategorySerializers



class ProductSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(read_only=True)
    category=CategorySerializers(many=False, read_only=True)
    
    class Meta:
        model=Product 
        fields='__all__'
        depth=1