from django.db import models
from django.contrib.auth import get_user_model
from category.models import ProductCategory
User = get_user_model()

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name="product_category")
    name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.DecimalField(max_digits=13, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    