from django.urls import path
from .views import wishlist_view, add_to_wishlist

urlpatterns = [
    path('', wishlist_view, name='wishlist'),
    path('add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
]