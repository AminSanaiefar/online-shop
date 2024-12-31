from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from products.models import Product


class Cart:
    def __init__(self, request):
        """
        Initialize The Cart
        """
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

        # if 'cart' not in request.session:
        #     self.cart = self.session['cart'] = {}
        # else:
        #     self.cart = self.session['cart']

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product_obj'] = product
        for item in cart.values():
            item['total_price'] = item['product_obj'].price * item['quantity']
            yield item

    def __len__(self):
        return sum(i['quantity'] for i in self.cart.values())

    def add(self, product, quantity=1, replace_current_quantity=False):
        """
        Add The Specified Product To The Cart If Exists
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}
        else:
            if replace_current_quantity:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] += quantity
        self.save()
        messages.success(self.request, _('Product successfully added to cart'))

    def remove(self, product):
        """
        Remove A Product From Cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            messages.success(self.request, _('Product successfully removed from cart'))

    def save(self):
        """
        Mark Session As Modified To Save Changes
        """
        self.session.modified = True

    def clear(self):
        del self.session['cart']
        self.save()

    def total_price(self):
        return sum(product['total_price'] for product in self.cart.values())
