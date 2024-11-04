from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
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
    
    @action(methods=["GET"], detail=True)
    def similar(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
            similar_products = product.get_similar_products()
            serializer = ProductSerializer(similar_products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)