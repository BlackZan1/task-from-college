from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

# models
from ..models import Car

# serializers
from .serializers import CarListSerializer

class CarsListCreateView(ListCreateAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    