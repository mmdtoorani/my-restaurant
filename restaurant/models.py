from django.contrib.auth.models import User
from django.db import models

from food.models import Food


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    IRANIAN = 'Iranian-restaurant'
    ITALIAN = 'Italian-restaurant'
    FRENCH = 'French-restaurant'
    CHINESE = 'Chinese-restaurant'
    FASTFOOD = 'fastfood'
    category_choice = (
        (IRANIAN, 'Iranian restaurant'),
        (ITALIAN, 'Italian restaurant'),
        (FRENCH, 'French restaurant'),
        (CHINESE, 'Chinese restaurant'),
        (FASTFOOD, 'fastfood')
    )
    category = models.CharField(
        max_length=30,
        choices=category_choice,
        help_text='please choose type of restaurant'
    )

    def __str__(self):
        return self.name


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


class Personnel(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, null=True, on_delete=models.SET_NULL)
    personnel_id = models.IntegerField(unique=True)

    SERVANT = 'servant'
    WAITER = 'waiter'
    CHEF = 'chef'
    MANAGER = 'manager'
    type_of_personnel_choice = (
        (SERVANT, 'servant'),
        (WAITER, 'waiter'),
        (CHEF, 'chef'),
        (MANAGER, 'manager'),
    )
    type_of_personnel = models.CharField(
        max_length=30,
        choices=type_of_personnel_choice,
        help_text='please select a position in personnel'
    )

    @property
    def restaurant_name(self):
        return self.branch.restaurant.name

    def __str__(self):
        return self.account.username


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
