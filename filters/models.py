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


class FilterImage(models.Model):
    id_image=models.AutoField(primary_key=True)
    filter=models.ForeignKey(Filter, default=None, blank=True, null=True)
    image=models.ImageField(upload_to="filters_images")
    is_active=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{0}".format(self.id_image)

    class Meta:
        verbose_name="Изображение"
        verbose_name_plural="Изображения"
