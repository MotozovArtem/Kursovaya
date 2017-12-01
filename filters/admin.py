from django.contrib import admin
from .models import *

class FilterAdmin(admin.ModelAdmin):
    list_filter = ["category", "brand"]
    search_fields = ["article", "category", "brand", "price"]
    list_display = ["article", "category", "brand", "price"]

admin.site.register(Filter, FilterAdmin)


class FilterImageAdmin(admin.ModelAdmin):
    list_filter = ["filter"]
    search_fields = ["filter"]
    list_display = ["filter", "is_active"]

admin.site.register(FilterImage, FilterImageAdmin)
