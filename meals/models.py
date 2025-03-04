from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meal(models.Model):

    MEAL_TYPES = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    )

    owner= models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)

    meal_type = models.CharField(max_length=10, choices=MEAL_TYPES)

    calories = models.IntegerField()

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name