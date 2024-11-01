from rest_framework import serializers
from .models import ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(
            max_length=None, use_url=True
        )
    class Meta:
        model = ProductImage
        fields = ("id", "img", "product", "get_image")
        read_only_field = ("get_image",)