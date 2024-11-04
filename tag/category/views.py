from rest_framework.viewsets import ModelViewSet
from .serializers import ProductCategorySerializer
from .models import ProductCategory
class ProductCategoryView(ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()




