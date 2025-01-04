from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address', 'order_note']
        widgets = {
            'address': forms.Textarea(attrs={
                'row': 4,
                'placeholder': _('write down your detailed address')
            }),
            'order_note': forms.Textarea(attrs={
                'row': 5,
                'placeholder': _('leave a note if you want')
            })
        }
