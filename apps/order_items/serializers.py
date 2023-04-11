from .models import OrderItem
from rest_framework import serializers



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=[
            'order', 
            'product',
            'quantity'
        ]
