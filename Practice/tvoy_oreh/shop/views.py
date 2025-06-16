from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Product, Order, OrderItem
from decimal import Decimal


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {
        'products': products,
        'cart_count': request.session.get('cart_count', 0)
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {
        'product': product,
        'cart_count': request.session.get('cart_count', 0)
    })


@login_required
def cart_view(request):
    order, created = Order.objects.get_or_create(
        user=request.user,
        status='P',
        defaults={'total_price': Decimal('0.00')}
    )
    return render(request, 'shop/cart.html', {
        'order': order,
        'cart_count': request.session.get('cart_count', 0)
    })


@require_POST
@login_required
def add_to_cart(request, pk):
    try:
        product = get_object_or_404(Product, pk=pk)
        order, created = Order.objects.get_or_create(
            user=request.user,
            status='P',
            defaults={'total_price': Decimal('0.00')}
        )

        order_item, created = OrderItem.objects.get_or_create(
            order=order,
            product=product,
            defaults={'price': product.price, 'quantity': 1}
        )

        if not created:
            order_item.quantity += 1
            order_item.save()

        order.total_price = sum(
            item.price * item.quantity
            for item in order.orderitem_set.all()
        )
        order.save()

        # Обновляем счетчик в сессии
        request.session['cart_count'] = order.orderitem_set.count()
        request.session.modified = True

        return JsonResponse({
            'success': True,
            'cart_total': order.orderitem_set.count(),
            'message': 'Товар добавлен в корзину'
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)


@require_POST
@login_required
def remove_from_cart(request, pk):
    try:
        order_item = get_object_or_404(OrderItem, pk=pk, order__user=request.user)
        order = order_item.order
        order_item.delete()

        order.total_price = sum(
            item.price * item.quantity
            for item in order.orderitem_set.all()
        )
        order.save()

        # Обновляем счетчик в сессии
        request.session['cart_count'] = order.orderitem_set.count()
        request.session.modified = True

        return JsonResponse({
            'success': True,
            'cart_total': order.orderitem_set.count(),
            'message': 'Товар удален из корзины'
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=400)