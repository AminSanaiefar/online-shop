from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products-list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('comment/<int:pid>', views.CommentCreateView.as_view(), name='comment-create'),
    path('addwish/<int:pk>', views.add_to_favorites, name='wishlist-add')
]
