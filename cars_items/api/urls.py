from django.urls import path

# views
from .views import CarsListCreateView

urlpatterns = [
    path('', CarsListCreateView.as_view(), name='car_list')
]