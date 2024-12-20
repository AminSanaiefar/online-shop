from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/products_list.html'
    context_object_name = 'products'

    # def get_queryset(self):
    #     return Product.objects.filter(active=True)


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
