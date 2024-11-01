from rest_framework import serializers
from .models import ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImage
        fields = ("id", "img", "product", "get_image_url")
        read_only_field = ("get_image_url",)

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.img.url)