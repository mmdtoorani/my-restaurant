from django.db import models


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

