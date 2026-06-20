from django.contrib import admin
from .models import Category, Product, Profile
from .models import Review
from .models import Newsletter

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Newsletter)