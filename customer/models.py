from django.contrib.auth.models import User
from django.db import models


class Customer(User):
    phone_number = models.CharField(max_length=12)
    # phone_number = models.CharField(regex=r'^\+?1?\d{9,15}$')


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField(max_length=250)


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
