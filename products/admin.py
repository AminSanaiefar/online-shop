from django.contrib import admin

from .models import Product, Comment, Discount, FavoriteProduct


class CommentsInline(admin.StackedInline):
    model = Comment
    classes = ['collapse']
    fields = ['user', 'text', 'rate', 'is_active']
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass


@admin.register(FavoriteProduct)
class FavoriteProductAdmin(admin.ModelAdmin):
    pass
