from django.db import models

# Create your models here.
class Category(models.Model):
    id_category=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"
        ordering=["id_category"]

    def __str__(self):
        return self.name
