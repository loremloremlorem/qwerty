from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from .models import Category, Product
from .models import Product, CartItem
from rest_framework import generics
from .models import Product, Category, CartItem, Order
from .serializers import ProductSerializer, CategorySerializer, CartItemSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken




@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category, 'categories': categories, 'products': products})

@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})

@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

@login_required
def cart_remove(request, product_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product_id=product_id)
    cart_item.delete()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'shop/cart/detail.html', {'cart_items': cart_items, 'total_price': total_price})



@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        return redirect('cart_detail')  

    order = Order.objects.create(user=request.user, paid=True) 
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            price=item.product.price,
            quantity=item.quantity
        )
    cart_items.delete() 
    return render(request, 'shop/order/confirmation.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'shop/order/history.html', {'orders': orders})



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            messages.error(request, "Пароли не совпадают!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Имя пользователя уже занято!")
            return redirect('register')

        user = User.objects.create_user(username=username,  password=password)
        login(request, user)
        return redirect('/')

    return render(request, 'shop/auth/register.html')


@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(request, 'shop/cart/detail.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'shop/order/history.html', {'orders': orders})


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        try:
            product = Product.objects.get(id=product_id)
            cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
            if not created:
                cart_item.quantity += int(quantity)
            cart_item.save()
            return Response({'message': 'Item added to cart'}, status=HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=HTTP_400_BAD_REQUEST)
    def delete(self, request):
        """Удаление товара из корзины или очистка корзины."""
        product_id = request.data.get('product_id')

    
        if product_id:
            try:
                cart_item = CartItem.objects.get(user=request.user, product_id=product_id)
                cart_item.delete()
                return Response({'message': 'Товар удалён из корзины'}, status=HTTP_204_NO_CONTENT)
            except CartItem.DoesNotExist:
                return Response({'error': 'Товар в корзине не найден'}, status=HTTP_400_BAD_REQUEST)


        CartItem.objects.filter(user=request.user).delete()
        return Response({'message': 'Корзина очищена'}, status=HTTP_204_NO_CONTENT)



class OrderDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, order_id=None):
        """Удаление заказа по ID."""
        if not order_id:
            return Response(
                {'error': 'Не указан ID заказа'},
                status=HTTP_400_BAD_REQUEST
            )

        try:
            # Получаем заказ по ID
            order = Order.objects.get(id=order_id)

            # Проверяем, что пользователь - владелец заказа или администратор
            if order.user != request.user and not request.user.is_staff:
                return Response(
                    {'error': 'Вы не можете удалить этот заказ'},
                    status=HTTP_400_BAD_REQUEST
                )

            # Проверяем, что заказ не оплачен
            if order.paid:
                return Response(
                    {'error': 'Нельзя удалить оплаченный заказ'},
                    status=HTTP_400_BAD_REQUEST
                )

            # Удаляем заказ
            order.delete()
            return Response(
                {'message': 'Заказ удалён'},
                status=HTTP_204_NO_CONTENT
            )

        except Order.DoesNotExist:
            return Response(
                {'error': 'Заказ не найден'},
                status=HTTP_400_BAD_REQUEST
            )

class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id=None):
        """Получение заказов пользователя или конкретного заказа."""
        if order_id:
            try:
                order = Order.objects.get(id=order_id, user=request.user)
                serializer = OrderSerializer(order)
                return Response(serializer.data, status=200)
            except Order.DoesNotExist:
                return Response({'error': 'Заказ не найден'}, status=400)

        # Список всех заказов пользователя
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=200)



class OrderListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [AllowAny()]

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [AllowAny()]

class LoginAPIView(APIView):
    def post(self, request):
        """Вход пользователя и получение токенов."""
        username = request.data.get('username')
        password = request.data.get('password')
        

        # Проверяем учетные данные
        user = authenticate(username=username, password=password)
        if user is not None:
            # Генерация токенов доступа
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=HTTP_200_OK)
        else:
            return Response(
                {'error': 'Неверное имя пользователя или пароль'},
                status=HTTP_400_BAD_REQUEST
            )