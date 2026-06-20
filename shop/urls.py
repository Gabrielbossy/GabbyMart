from django.urls import path
from .views import home, product_detail, search_products, profile, support, faq, subscribe, notifications, dashboard

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('search/', search_products, name='search'),
    path('support/', support, name='support'),
    path('faq/', faq, name='faq'),
    path(
    'subscribe/',
    subscribe,
    name='subscribe'
    
),
    path(
    'notifications/',
    notifications,
    name='notifications'
),
    path(
    'dashboard/',
    dashboard,
    name='dashboard'
),
    
]