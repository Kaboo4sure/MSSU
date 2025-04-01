from django.db import models
from users.models import CustomUser

class Product(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'seller'})
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='product_images/')
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

