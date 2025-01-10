from django.urls import path
from .views import ProductListAPIView, ProductDetailAPIView, CartAPIView, OrderListAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='api_product_list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='api_product_detail'),
    path('cart/', CartAPIView.as_view(), name='api_cart'),
    path('orders/', OrderListAPIView.as_view(), name='api_order_list'),
]
