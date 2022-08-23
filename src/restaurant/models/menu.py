from django.db import models
from .branch import Branch

from food.models import Food


class Menu(models.Model):
    branch = models.OneToOneField(Branch, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.branch.name}'s Menu"


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    food = models.OneToOneField(Food, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.food.name} | {self.menu.branch.name}"
