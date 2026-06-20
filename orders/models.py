from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Processing', 'Processing'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name