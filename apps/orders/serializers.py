from apps import users
from apps.users.serializers import UserSerializer
from .models import Order
from rest_framework import serializers
from apps.order_items.models import OrderItem
from apps.order_items.serializers import OrderItemSerializer





class OrderSerializer(serializers.ModelSerializer):
    order_items=OrderItemSerializer(many=True)
    class Meta:
        model=Order
        fields=[
            'user', 
            'customer_name',
            'customer_phone',
            'customer_address',
            'zip_code',
            'building',
            'city',
            'state',
            'total_price',
            'total_qty'

        ]

    def create(self, validated_data):
        order_items=validated_data.pop('order_items')
        order=Order.objects.create(**validated_data)
        for item in order_items:
            OrderItem.objects.create(**item, order=order)

        return order
    
class OrderListSerializer(serializers.ModelSerializer):
    order_items=OrderItemSerializer(many=True)
    class Meta:
        model=Order
        fields=[
            'user', 
            'customer_name',
            'customer_phone',
            'customer_address',
            'zip_code',
            'building',
            'city',
            'state',
            'total_price',
            'total_qty'

        ]