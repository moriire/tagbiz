from rest_framework import serializers
from .models import ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = ProductImage
        fields = ("id", "img", "product", "image_url")
        read_only_field = ("image_url",)

    def get_image_url(self, obj):
        #request = self.context.get("request")
        return self.build_url_field(ProductImage, "img")