from django.db import models
from categories.models import Category
from brands.models import Brand


# Create your models here.
class Filter(models.Model):
    id_filter = models.AutoField(primary_key=True)
    article = models.CharField(verbose_name="Артикул", max_length=100, default=None, unique=True)
    category = models.ForeignKey(Category, verbose_name="Категория", default=None)
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    brand = models.ForeignKey(Brand, verbose_name="Производитель", default=None)
    description = models.TextField(verbose_name="Описание", default=None, blank=True, null=True)
    specific = models.TextField(verbose_name="Характеристики", default=None, blank=True, null=True)
    price = models.DecimalField(verbose_name="Цена", max_digits=8, decimal_places=2, blank=True, null=True, default=0)
    is_active = models.BooleanField(verbose_name="Активен", default=True)
    is_popular = models.BooleanField(verbose_name="Входит в топ продаж", default=False)
    # count=models.IntegerField(default=0, verbose_name="Кол-во проданных")
    sale = models.DecimalField(verbose_name="Cкидка", default=0, decimal_places=2, max_digits=8)
    discount = models.IntegerField(default=0, verbose_name="Скидка в процентах")
    is_new = models.BooleanField(verbose_name="Новинка", default=False)
    new_price = models.DecimalField(verbose_name="Цена со скидкой", max_digits=8, decimal_places=2, blank=True,
                                    null=True, default=0)

    # created=models.DateTimeField(auto_now_add=True, auto_now=False, default=)

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.article, self.category, self.brand, self.price)

    class Meta:
        verbose_name = "Фильтр"
        verbose_name_plural = "Фильтры"

    def save(self, *args, **kwargs):
        if self.discount > 0:
            self.new_price = self.price - self.price * self.discount / 100
            self.sale = self.discount / 100
        if self.category.name == "Топливные фильтры":
            self.name = "Топливный фильтр"
        elif self.category.name == "Воздушные фильтры":
            self.name = "Воздушный фильтр"
        elif self.category.name == "Гидравлические фильтры":
            self.name = "Гидравлический фильтр"
        elif self.category.name == "Масляные фильтры":
            self.name = "Масляный фильтр"
        elif self.category.name == "Топливные сепараторы":
            self.name = "Топливный сепаратор"
        elif self.category.name == "Фильтры осушителя":
            self.name = "Фильтр осушителя"
        elif self.category.name == "Пневморессоры":
            self.name = "Пневморессор"
        elif self.category.name == "Фильтры охлаждающей жидкости":
            self.name = "Фильтр системы охлаждения"
        elif self.category.name == "Фильтры карбамидные AdBlue":
            self.name = "Фильтр карбамидный AdBlue"
        super(Filter, self).save(*args, **kwargs)


class FilterImage(models.Model):
    id_image = models.AutoField(primary_key=True)
    filter = models.ForeignKey(Filter, default=None, blank=True, null=True, verbose_name="Фильтр")
    image = models.ImageField(upload_to="filters_images")
    is_active = models.BooleanField(verbose_name="Активен", default=True)
    is_main = models.BooleanField(verbose_name="Главная", default=False)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name="Отредактирован", auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{0}".format(self.id_image)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
