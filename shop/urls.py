from django.urls import path, include   
from . import views
from django.contrib.auth import views as auth_views
from shop.swagger import schema_view
from shop.views import LoginWithCSRFAPIView

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('categories/', views.categories, name='categories'),
    path('contacts/', views.contacts, name='contacts'),
    path('detail/', views.detail, name='detail'),
    path('categories/products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),


    path('swagger/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    # path('orders/', views.order_history, name='order_history'),
    # path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    # path('cart/delete/<int:product_id>/', views.cart_remove, name='cart_remove'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    # path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('login/', LoginWithCSRFAPIView.as_view(), name='api_login_with_csrf'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    # path('register/', views.register, name='register'),
    # path('api/', include('shop.api_urls')),
]




