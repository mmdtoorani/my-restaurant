from django.db import models
from .category import Category


class Food(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
