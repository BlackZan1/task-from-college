from rest_framework.serializers import ModelSerializer

# models
from ..models import Car

class CarListSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'name',
            'price',
            'description',
            'images'
        )

class CarDetailSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'