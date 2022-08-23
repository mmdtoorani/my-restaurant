from django.db import models
from .customer import Customer


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.username}'s Cart"
