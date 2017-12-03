from django.db import models
from filters.models import Filter
from django.db.models.signals import post_save


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
    total_price=models.DecimalField(max_digits=10, decimal_places=2, default=0.00) #Общая стоимость заказа
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


    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    id_productInOrder = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, default=None, blank=True, null=True)
    numb=models.IntegerField(default=1)
    price_item=models.DecimalField(max_digits=10, decimal_places=2, default=0) #За сколько продали
    total_price=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)#Общая стоимость на товар(кол-во*цену
    product = models.ForeignKey(Filter, default=None, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Товар в заказе {0} {1}".format(self.product.category, self.product.article)

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    def save(self, *args, **kwargs):
        self.price_item=self.product.price
        self.total_price=self.price_item*self.numb

        super(ProductInOrder, self).save(*args, **kwargs)



#Главное не сохранять в пост save сигнале данные в моделе, после которой вызывается сигнал, иначе получится зацикливание
def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)





