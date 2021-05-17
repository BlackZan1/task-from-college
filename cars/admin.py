from django.contrib import admin

# models
from .models import Car #, CustomImageModel

# Register your models here.
admin.site.register(Car)
# admin.site.register(CustomImageModel)