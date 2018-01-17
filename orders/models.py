from django.db import models
from filters.models import Filter
from django.db.models.signals import post_save


# Create your models here.

class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Статус", max_length=100, default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Статусы закакза"
        verbose_name = "Статус заказа"

    def __str__(self):
        return "{0}".format(self.name)


class Order(models.Model):
    total_price = models.DecimalField(verbose_name="Итого", max_digits=10, decimal_places=2,
                                      default=0)  # Общая стоимость заказа
    id_order = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=120, verbose_name="Имя", default=None)
    customer_email = models.EmailField(verbose_name="Email")
    customer_phone = models.CharField(verbose_name="Телефон", max_length=25, default=None)
    status = models.ForeignKey(Status, verbose_name="Статус заказа", default=2)
    comments = models.TextField(verbose_name="Комментарии к заказу", default=None, blank=True, null=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name="Изменен", auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ: {0} {1} {2} {3}".format(self.customer_name, self.customer_email,
                                                   self.customer_phone, self.status)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    id_productInOrder = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, verbose_name="Заказ", default=None)
    numb = models.IntegerField(default=1, verbose_name="Кол-во")
    price_item = models.DecimalField(verbose_name="Цена продажи на данный момент", max_digits=10, decimal_places=2,
                                     default=0)  # За сколько продали
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                      verbose_name="Сумма")  # Общая стоимость на товар(кол-во*цену
    product = models.ForeignKey(Filter, verbose_name="Фильтр", default=None)
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создан")
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Изменен")

    def __str__(self):
        return "Товар в заказе {0} {1} {2} {3} {4} {5}".format(self.order.customer_name, self.product.article,
                                                               self.product.category, self.product.brand, self.numb,
                                                               self.total_price)

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    def save(self, *args, **kwargs):
        if self.product.discount > 0:
            self.price_item = self.product.new_price
        else:
            self.price_item = self.product.price

        self.total_price = self.price_item * int(self.numb)

        super(ProductInOrder, self).save(*args, **kwargs)
