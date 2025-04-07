from django.contrib.auth.decorators import login_required
from .models import Order
from django.shortcuts import render, redirect
from .models import OrderItem

@login_required
def my_orders(request):
    orders = Order.objects.filter(buyer=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})


@login_required
def seller_orders(request):
    if request.user.role != 'seller':
        return redirect('home')

    order_items = OrderItem.objects.filter(product__seller=request.user).select_related('order', 'product').order_by('-order__order_date')


    return render(request, 'orders/seller_orders.html', {
        'order_items': order_items
    })

