from django.contrib import admin

from .models import Order, OrderItem


class OrderItemsInline(admin.StackedInline):
    model = OrderItem
    classes = ['collapse']
    fields = ['order', 'product', 'price', 'quantity']
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemsInline,
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity', 'total_price']

    def total_price(self, obj):
        return obj.quantity * obj.price
