from django.db import models
from apps.products.models import Product
from apps.orders.models import Order
from django.utils import timezone
from django.db.models.deletion import CASCADE
# Create your models here.


class OrderItem(models.Model):
    class Meta(object):
        db_table='order_items'

    order=models.ForeignKey(
     Order,related_name="realted_order",on_delete=CASCADE

    )
    product=models.ForeignKey(
        Product, related_name='related_order_item_product', on_delete=models.CASCADE
    )
    qty=models.IntegerField(
        'quantity', blank=False, null=False
    )
    created_at=models.DateTimeField(
       'created', blank=True, default=timezone.now 
    )