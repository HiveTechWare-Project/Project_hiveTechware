from django.db import models
from apps.users.models import User
from django.utils import timezone
# Create your models here.


class Order(models.Model):
    class Meta(object):
        db_table='orders'

    user=models.ForeignKey(
        User, on_delete=models.CASCADE,related_name='related_order_user'
    )

    customer_name=models.CharField(
        'Customer Name', blank=False, null=False, max_length=200
    )

    customer_phone=models.CharField(
        'Customer Phone', blank=False, null=False, max_length=20
    )

    customer_address=models.CharField(
        'Customer Address', blank=False, null=False, max_length=150
    )

    zip_code=models.CharField(
        'Zip Code', blank=False, null=False, max_length=100
    )

    building=models.CharField(
        'Building', blank=False, null=False, max_length=150
    )

    city=models.CharField(
        'City', blank=False, null=False, max_length=120
    )

    state=models.CharField(
        'State', blank=False, null=False, max_length=150
    )
    total_price=models.FloatField(
        'Total Price', blank=False, null=False
    )
    total_qty=models.IntegerField(
        'Total Quantity', blank=False, null=False
    )
    created_at=models.DateTimeField(
        'creation Date', blank=True, default=timezone.now
    )

    @property
    def order_items(self):
        return self.related_order.all()
    
