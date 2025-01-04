from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .forms import OrderForm
from .models import OrderItem
from cart.cart import Cart


@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if not cart:
        messages.warning(request, _('you must add some stuff to your cart first'))
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            form_obj = order_form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()
            order_form = OrderForm()

            for item in cart:
                OrderItem.objects.create(
                    order=form_obj,
                    product=item['product_obj'],
                    price=item['product_obj'].price,
                    quantity=item['quantity']
                )
            cart.clear()

            request.user.first_name = form_obj.first_name
            request.user.last_name = form_obj.last_name
            request.user.save()
            messages.success(request, _('your order has successfully placed.'))

            return redirect('home')

    return render(request, 'orders/order_create.html', context={
        'form': order_form,
    })
