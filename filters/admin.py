from django.contrib import admin
from .models import Filter

class FilterAdmin(admin.ModelAdmin):
    list_filter = ["category", "brand"]
    search_fields = ["article", "category", "brand", "price"]
    list_display = ["article", "category", "brand", "price"]

admin.site.register(Filter, FilterAdmin)
