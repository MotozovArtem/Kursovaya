from django.db import models
from categories.models import Category
from brands.models import Brand


# Create your models here.
class Filter(models.Model):
    id_filter = models.AutoField(primary_key=True)
    article = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    brand = models.ForeignKey(Brand)
    description = models.TextField()
    specific = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    image=models.CharField(max_length=255, null=True)

