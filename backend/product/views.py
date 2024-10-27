from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().select_related()

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        if slug:
            self.queryset = self.queryset.filter(category__slug= slug)

        return self.queryset




