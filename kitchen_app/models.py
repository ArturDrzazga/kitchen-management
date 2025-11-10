from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from kitchen_management import settings


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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
    ingredients = models.ManyToManyField(Ingredient, related_name="dish_ingredients")
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")

    def clean(self):
        super().clean()

        if self.price is not None and self.price <= 0:
            raise ValidationError("Price must be grater than 0")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.price}"