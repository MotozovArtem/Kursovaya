from django.db import models
from filters.models import Filter
# Create your models here.
class Order(models.Model):
    id_order=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=120, default=None, blank=True, null=True)
    customer_email=models.EmailField(default=None, blank=True, null=True)
    customer_phone=models.CharField(max_length=100, default=None, blank=True, null=True)
    comments=models.TextField(default=None, blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ: {0} {1}".format(self.id_order, self.customer_name)
    class Meta:
        verbose_name="Заказ"
        verbose_name_plural="Заказы"

class ProductInOrder(models.Model):
    id_productInOrder=models.AutoField(primary_key=True)
    order=models.ForeignKey(Order, default=None, blank=True, null=True)
    product=models.ForeignKey(Filter, default=None, blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Товар в заказе {0} {1}".format(self.product.category,self.product.article)

    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товары"