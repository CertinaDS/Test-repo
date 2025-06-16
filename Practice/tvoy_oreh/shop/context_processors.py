from .models import Order

def cart_context(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Order.objects.filter(
            user=request.user,
            status='P'
        ).count()
    return {
        'cart_count': request.session.get('cart_count', cart_count)
    }