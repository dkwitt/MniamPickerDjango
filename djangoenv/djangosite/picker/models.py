from django.db import models

# Create your models here.
class Meals(models.Model):
    name = models.CharField(max_length=200)
    carbs = models.CharField(max_length=200)
    meat = models.CharField(max_length=200)
    side_dish = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)
