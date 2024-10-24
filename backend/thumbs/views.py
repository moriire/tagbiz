from rest_framework.viewsets import ModelViewSet
from .models import ProductImage
from .serializers import ProductImageSerializer

class ProductImageView(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer