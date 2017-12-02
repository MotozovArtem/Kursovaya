from django.db import models
from filters.models import Filter


# Create your models here.

class Status(models.Model):
    id_status=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural="Статусы закакза"
        verbose_name="Статус заказа"

    def __str__(self):
        return "{0}".format(self.name)



class Order(models.Model):
    total_price=models.DecimalField(max_digits=10, decimal_places=2, default=0) #Общая стоимость заказа
    id_order = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=120, default=None, blank=True, null=True)
    customer_email = models.EmailField(default=None, blank=True, null=True)
    customer_phone = models.CharField(max_length=100, default=None, blank=True, null=True)
    status = models.ForeignKey(Status)
    comments = models.TextField(default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ: {0} {1} {2}".format(self.id_order, self.customer_name, self.status)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class ProductInOrder(models.Model):
    id_productInOrder = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, default=None, blank=True, null=True)
    numb=models.IntegerField(default=1)
    price_item=models.DecimalField(max_digits=10, decimal_places=2, default=0) #Цена, по которой продали товар
    total_price=models.DecimalField(max_digits=10, decimal_places=2, default=0)#Общая стоимость на товар(кол-во*цену
    product = models.ForeignKey(Filter, default=None, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Товар в заказе {0} {1}".format(self.product.category, self.product.article)

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"




