from django.db import models


# Create your models here.
class Brand(models.Model):
    id_brand = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Производитель",max_length=100)
    is_active=models.BooleanField(verbose_name="Активный", default=True)

    class Meta:
        verbose_name_plural="Бренды"
        verbose_name="Бренд"

    def __str__(self):
        return self.name

class BrandImage(models.Model):
    id_image=models.AutoField(primary_key=True)
    brand=models.ForeignKey(Brand, default=None, blank=True, null=True, verbose_name="Бренд")
    image=models.ImageField(upload_to="brand_images")
    is_active=models.BooleanField(verbose_name="Активен",default=True)
    is_main = models.BooleanField(verbose_name="Главная",default=False)
    created = models.DateTimeField(verbose_name="Создан",auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name="Отредактирован",auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{0}".format(self.id_image)

    class Meta:
        verbose_name="Изображение"
        verbose_name_plural="Изображения"