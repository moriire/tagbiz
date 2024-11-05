from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import LimitOffsetPagination

class ProductPagination(LimitOffsetPagination):
    default_limit = 6
    max_limit = 12
    min_limit = 1
    min_offset = 0
    max_offset = 1000000

class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().select_related()
    pagination_class = ProductPagination

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        if slug:
            self.queryset = self.queryset.filter(category__slug= slug)
        return self.queryset
    
    @action(methods=["GET"], detail=False)
    def latest(self, request):
        items = self.get_queryset()[:12]
        ser = ProductSerializer(items, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    
    @action(methods=["GET"], detail=True)
    def similar(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
            similar_products = product.get_similar_products()
            serializer = ProductSerializer(similar_products)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)