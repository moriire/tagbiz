
from rest_framework import serializers
from .models import ProductCategory
from thumbs.serializers import ProductImageSerializer

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
       