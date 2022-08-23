from django.contrib.auth.models import User
from django.db import models
from .branch import Branch


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
