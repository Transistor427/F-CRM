from django.db import models

# Create your models here.

class Parts(models.Model):
    name = models.CharField(max_length=100)
    module = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to=None, height_field=500, width_field=500, max_length=100)
