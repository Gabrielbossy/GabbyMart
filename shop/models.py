from django.db import models
from django.contrib.auth.models import User


# Product Categories
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Products
class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)

    price = models.IntegerField()

    description = models.TextField()

    image = models.ImageField(upload_to='products/')

    stock = models.IntegerField(default=1)

    available = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username


# Review and Rating
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField(default=5)
    comment = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    
class Newsletter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email  
    
    
class Notification(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    message = models.CharField(max_length=255)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.message     