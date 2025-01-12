from django.urls import path, include   
from . import views
from django.contrib.auth import views as auth_views
from shop.swagger import schema_view
from shop.views import LoginWithCSRFAPIView

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('checkout/', views.checkout, name='checkout'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('orders/', views.order_history, name='order_history'),
    path('login/', LoginWithCSRFAPIView.as_view(), name='api_login_with_csrf'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('api/', include('shop.api_urls')),
]




