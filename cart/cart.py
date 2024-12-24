from products.models import Product


class Cart:
    def __init__(self, request):
        """
        Initialize The Cart
        """
        self.request = request
        self.session = request.seesion
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product_obj'] = product
        for item in cart.values():
            yield item

    def __len__(self):
        return len(self.cart.keys())

    def add(self, product, quantity=1):
        """
        Add The Specified Product To The Cart If Exists
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}
        else:
            self.cart[product_id]['quantity'] += quantity
            self.save()

    def remove(self, product):
        """
        Remove A Product From Cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        """
        Mark Session As Modified To Save Changes
        """
        self.session.modified = True

    def clear(self):
        del self.session['cart']
        self.save()

    def total_price(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return sum(product.price for product in products)
