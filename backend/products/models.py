from django.db import models
from wholesalers.models import Wholesaler

# Create your models here.
class Product(models.Model):
    name = models.ForeignKey(Wholesaler, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    product_image = models.ImageField(default="product.jpeg", upload_to="product-images", blank=False)
    price = models.IntegerField()
    description = models.TextField(max_length=200, blank=False)
    