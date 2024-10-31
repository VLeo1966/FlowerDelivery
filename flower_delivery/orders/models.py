# orders/models.py
from django.db import models
from django.contrib.auth.models import User
from catalog.models import flower

class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(flower, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.pk} by {self.user.username}"

