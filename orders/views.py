from django.shortcuts import render, redirect
from .models import Order


def checkout(request):

    if request.method == 'POST':

        full_name = request.POST['full_name']
        phone = request.POST['phone']
        address = request.POST['address']

        Order.objects.create(
            customer=request.user,
            full_name=full_name,
            phone=phone,
            address=address,
            total_price=0
        )

        return redirect('order_success')

    return render(request, 'checkout.html')


def my_orders(request):

    orders = Order.objects.filter(
        customer=request.user
    ).order_by('-created_at')

    return render(
        request,
        'my_orders.html',
        {'orders': orders}
    )


def order_success(request):
    return render(request, 'order_success.html')