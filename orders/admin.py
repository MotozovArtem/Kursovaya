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
    list_display = ["customer_name", "status","created"]

admin.site.register(Order, OrderAdmin)

class ProductInOrderAdmin(admin.ModelAdmin):
    list_filter = ["order", "product"]
    search_fields = ["product"]
    list_display = ["order", "product"]

admin.site.register(ProductInOrder, ProductInOrderAdmin)
admin.site.register(Status)