
from rest_framework import serializers
from .models import Product
from category.serializers import ProductCategorySerializer
from thumbs.models import ProductImage
from thumbs.serializers import ProductImageSerializer

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False, read_only=True)
    uploads = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )
    category = ProductCategorySerializer()
    class Meta:
        model = Product
        fields = ("id", "name", "description", "category", "price", "images", "uploads", "discount", "discounted_price", "new_price")

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        Product = Product.objects.create(**validated_data)
        for image_data in images_data:
            ProductImage.objects.create(product=Product, **image_data)
        return Product