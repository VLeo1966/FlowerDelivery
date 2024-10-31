from django.db import models
from django.contrib.auth import get_user_model
from flower_catalog.models import Flower

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    delivery_address = models.CharField(max_length=255)
    delivery_date = models.DateTimeField()

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
