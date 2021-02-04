from django.db import models

# Create your models here.
class Product(models.Model): #I inheritted some functions and attributes from models.Model
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()