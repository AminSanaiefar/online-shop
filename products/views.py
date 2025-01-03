from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product, Comment
from .forms import CommentForm


class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/products_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        # context['add_to_cart_form'] = AddToCartProductForm()
        return context


@login_required
def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.order_by('-datetime_created')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, 'products/product_detail.html',
                  context={'product': product,
                           'comments': comments,
                           'comment_form': comment_form
                           })


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        pid = int(self.kwargs['pid'])
        product = get_object_or_404(Product, pk=pid)
        obj.product = product
        obj.save()
        messages.success(self.request, messages.INFO, _("Comment Sent!"))
        return super().form_valid(form)
