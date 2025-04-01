from django.db import models
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    low_stock_threshold = models.PositiveIntegerField(default=5)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def is_low_stock(self):
        return self.quantity > 0 and self.quantity <= self.low_stock_threshold

    def is_out_of_stock(self):
        return self.quantity == 0

    def __str__(self):
        return self.name
