from django.contrib import admin
from orders.models import *


# Register your models here.

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInOrderInline]
    list_filter = ["status", "customer_name"]
    search_fields = ["status", "customer_name"]
    list_display = ["customer_name", "customer_email", "customer_phone", "status", "created"]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)
admin.site.register(Status)
