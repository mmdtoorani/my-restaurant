from django.contrib.auth.models import User
from django.db import models


class Customer(User):
    phone_number = models.CharField(max_length=12)
    # phone_number = models.CharField(regex=r'^\+?1?\d{9,15}$')

    def __str__(self):
        return self.username
