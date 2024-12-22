from django.contrib import admin

from .models import Product, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'datetime_created', 'active']


@admin.register(Comment)
class ModelNameAdmin(admin.ModelAdmin):
    pass
