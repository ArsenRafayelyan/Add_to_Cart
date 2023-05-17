from django.db import models

# Create your models here.

class Product(models.Model):

    name = models.CharField('product name',max_length=300)
    price = models.PositiveIntegerField('product price')
    img = models.ImageField('product img',upload_to='media')

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    cart_item = models.ForeignKey(Product, on_delete=models.CASCADE)

    