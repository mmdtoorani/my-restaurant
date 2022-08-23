from django.db import models
from .restaurant import Restaurant


class Branch(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=250)
    city = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    description = models.TextField(max_length=250, null=True, blank=True)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

