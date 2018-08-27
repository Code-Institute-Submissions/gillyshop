from django.db import models

# Create your models here.
# class Product(models.Model):
#     name = models.CharField(max_length=254, default='')
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     image = models.ImageField(upload_to='images')
    
    # def __str__(self):
    #     return self.name

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # userid = models.ForeignKey(admin, related_name='userblogpost')
    Picture = None


class Picture(models.Model):
    picture = models.ImageField(upload_to='images')
    productid = models.ForeignKey('Product')
    
    
    def __unicode__(self):
        return self.title
        

        
