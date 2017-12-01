from django.contrib import admin
from orders.models import *
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_filter = ["status", "customer_name"]
    search_fields = ["status", "customer_name"]
    list_display = ["customer_name", "status"]

admin.site.register(Order, OrderAdmin)


admin.site.register(ProductInOrder)