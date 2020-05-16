from django.contrib import admin

from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'date_updated', 'is_published']
    list_filter = ['is_published']
    search_fields = ['title']
    readonly_fields = ['date_created', 'date_updated']

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_title', 'quantity', 'date_created']

    def product_title(self, obj):
        return obj.product.title
