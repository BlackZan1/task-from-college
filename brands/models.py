from django.db import models

# utils
from core.upload_rename import upload_rename

# Create your models here.
class Brand(models.Model):
    image = models.ImageField(upload_to = upload_rename('brands'))
    name = models.CharField(max_length = 50)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name