from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    class Meta(object):
        db_table='category'


    name = models.CharField(
        "name",blank=False,null=False,max_length=100,db_index=True
    )
    image = CloudinaryField(
        'image', blank=True, null=True
    )

    created_at= models.DateTimeField(
        'creation_date', blank=True, null=True, auto_now_add=True 
    )

    updated_at=models.DateTimeField(
        'updated_at', blank=True, null=True, auto_now=True
    )

    def __str__(self):
        return self.name
    