from django.contrib.auth.models import AbstractUser
from django.db import models

class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name} username: {self.username}"


class DishType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    cooks = models.ManyToManyField(Cook)

    def __str__(self):
        return self.name