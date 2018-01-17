from django.contrib import admin
from .models import *


class BrandImageInline(admin.TabularInline):
    model = BrandImage
    extra = 0

class BrandAdmin(admin.ModelAdmin):
    inlines = [BrandImageInline]

admin.site.register(Brand, BrandAdmin)


class BrandImageAdmin(admin.ModelAdmin):

    list_display = ["brand", "is_active"]

admin.site.register(BrandImage, BrandImageAdmin)
