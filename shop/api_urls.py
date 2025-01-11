from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView, CartAPIView, OrderListAPIView
from .views import CategoryListCreateAPIView, CategoryDetailAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='api_product_list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='api_product_detail'),
    path('cart/', CartAPIView.as_view(), name='api_cart'),
    path('orders/', OrderListAPIView.as_view(), name='api_order_list'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='api_category_list_create'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='api_category_detail'),
]


