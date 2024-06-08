from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wholesaler(models.Model):
    wholesaler_name = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=200, blank=False)
    banner = models.ImageField(default="location.png", upload_to="wholesaler-images", blank=False)

    def __str__(self):
        return self.wholesaler_name
    
    
