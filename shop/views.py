from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Profile, Review
from .forms import ProfileForm, ReviewForm
from django.db.models import Q
from .models import Newsletter
from .models import Notification
from django.contrib.auth.models import User
from orders.models import Order



def home(request):
    products = Product.objects.all()

    return render(request, 'home.html', {
        'products': products
    })


@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()

    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {
        'profile': profile,
        'form': form
    })
    
    
def search_products(request):
    query = request.GET.get('q')

    products = []

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query)
        )

    return render(request, 'search.html', {
        'products': products,
        'query': query
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)

            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
        else:
            form = ReviewForm()

    else:
        form = ReviewForm()

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form
    })
    
def support(request):
    return render(request, 'support.html')   

def faq(request):
    return render(request, 'faq.html')

def subscribe(request):

    if request.method == "POST":

        email = request.POST['email']

        Newsletter.objects.get_or_create(
            email=email
        )

        messages.success(
            request,
            "You have successfully subscribed to the Mali Tap newsletter."
        )

    return redirect('/')

def notifications(request):

    notices = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'notifications.html', {
        'notifications': notices
    })
    
    
@login_required
def dashboard(request):

    total_products = Product.objects.count()
    total_users = User.objects.count()
    total_orders = Order.objects.count()
    total_reviews = Review.objects.count()

    context = {
        'total_products': total_products,
        'total_users': total_users,
        'total_orders': total_orders,
        'total_reviews': total_reviews,
    }

    return render(
        request,
        'dashboard.html',
        context
    )    




    