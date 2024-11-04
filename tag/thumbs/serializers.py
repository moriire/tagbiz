from rest_framework import serializers
from .models import ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(use_url = True)

    class Meta:
        model = ProductImage
        fields = ("id", "img", "product")#, "image_url")
        #read_only_field = ("image_url",)