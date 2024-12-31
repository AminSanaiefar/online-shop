from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail_view, name='cart-detail'),
    path('add/<int:product_id>', views.add_to_cart_view, name='add-to-cart'),
    path('remove/<int:product_id>', views.remove_from_cart, name='remove-product'),
]
