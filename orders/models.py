from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE, 'user', verbose_name=_('User'))
    is_paid = models.BooleanField(default=False, verbose_name=_('Is Paid'))
    first_name = models.CharField(max_length=150, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=150, verbose_name=_('Last Name'))
    phone = models.CharField(max_length=11, verbose_name=_('Phone Number'))
    address = models.CharField(max_length=650, verbose_name=_('Address'))
    order_note = models.CharField(max_length=500, blank=True, verbose_name=_('Note'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order: {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, models.CASCADE, 'items')
    product = models.ForeignKey(Product, models.CASCADE)
    price = models.PositiveIntegerField(_('Price'))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_('Quantity'))

    def __str__(self):
        return f'{self.product} X {self.quantity} [total price:{self.quantity * self.price}]'
