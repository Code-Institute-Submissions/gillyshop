from django.db import models
from taggit.managers import TaggableManager

# Code below half mine/half adapted from lessons

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', blank=False)
    imagetwo = models.ImageField(upload_to='images', blank=True)
    tags = TaggableManager()
    category = models.CharField(max_length=100, default='')

    
    
    def __str__(self):
        return self.name
        
        
        

        
