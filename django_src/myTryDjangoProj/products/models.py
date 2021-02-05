from django.db import models

# Create your models here.
class Product(models.Model): #I inheritted some functions and attributes from models.Model
    title       = models.CharField(max_length=120) # max_length is required in CharField
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=100)
    summary     = models.TextField(default='this is cool')
    featured    = models.BooleanField(null=True, default=False) #null=True, default
