from django.shortcuts import render, redirect
from .models import CartItem
from shop.models import Product

def cart_view(request):

    items = CartItem.objects.filter(user=request.user)

    return render(request, 'cart.html', {
        'items': items
    })
    
def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('/cart/')

def remove_from_cart(request, item_id):

    item = CartItem.objects.get(id=item_id)

    item.delete()

    return redirect('/cart/')