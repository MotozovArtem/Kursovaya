from django.db import models
from categories.models import Category
from brands.models import Brand


# Create your models here.
class Filter(models.Model):
    id_filter = models.AutoField(primary_key=True)
    article = models.CharField(max_length=100, default=None, blank=True, null=True)
    category = models.ForeignKey(Category, default=None, blank=True, null=True)
    brand = models.ForeignKey(Brand, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    specific = models.TextField(default=None, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=None, blank=True, null=True)
    in_stock = models.BooleanField(default=True)


    class Meta:
        verbose_name="Фильтр"
        verbose_name_plural="Фильтры"



