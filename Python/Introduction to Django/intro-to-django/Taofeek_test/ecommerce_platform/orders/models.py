from django.db import models
from users.models import CustomUser
from products.models import Product

class Order(models.Model):
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'buyer'})
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Processing')  # Can be 'Shipped', 'Returned', etc.

    def __str__(self):
        return f"Order #{self.id} by {self.buyer.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # price at time of order

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"
