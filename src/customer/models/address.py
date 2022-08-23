from django.db import models
from .customer import Customer


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.customer.username}'s Address"

