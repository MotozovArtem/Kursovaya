from django.db import models


# Create your models here.
class Brand(models.Model):
    id_brand = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)