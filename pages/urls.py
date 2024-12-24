from django.urls import path

from . import views
from products.views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('aboutus/', views.AboutUsView.as_view(), name='aboutus')
]
