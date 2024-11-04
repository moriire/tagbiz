from rest_framework.viewsets import ModelViewSet
from .serializers import LocationSerializer, Location

class LocationView(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()




