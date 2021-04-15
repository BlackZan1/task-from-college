from django.db import models

# models
from brands.models import Brand

# utils
from core.upload_rename import upload_rename

class CustomImageModel(models.Model):
    url = models.ImageField(upload_to = upload_rename('cars'))
    name = models.CharField(max_length = 100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Car(models.Model):
    class CarStatusChoices(models.TextChoices):
        NEW = 'new'
        USED = 'used'
        SOON = 'soon'

    class CarTypesChoices(models.TextChoices):
        AUTO = 'Автомобиль'

    class CarGearboxesChoices(models.TextChoices):
        AUTO = 'Автоматический'

    name = models.CharField(max_length = 50)
    price = models.IntegerField(null = True, blank = True)
    images = models.ManyToManyField(CustomImageModel)
    description = models.TextField()
    publish_date = models.DateField(null = True, blank = True)
    brand = models.ForeignKey(Brand, on_delete = models.SET_NULL, null = True, blank = True)
    model_type = models.CharField(max_length = 50, null = True, blank = True)
    status = models.CharField(choices = CarStatusChoices.choices, default = CarStatusChoices.SOON, max_length = 4)
    car_type = models.CharField(choices = CarTypesChoices.choices, default = CarTypesChoices.AUTO, max_length = 50)
    gearbox = models.CharField(choices = CarGearboxesChoices.choices, default = CarGearboxesChoices.AUTO, max_length = 50)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
    