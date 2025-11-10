from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from kitchen_app.models import DishType, Ingredient, Dish


class ModelTests(TestCase):
    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="cooktest",
            first_name="test",
            last_name="test",
            password="test123",
            years_of_experience= 5
        )

        self.assertEqual(str(cook), f"{cook.first_name} {cook.last_name}")

    def test_cook_valid_years_of_experience(self):

        with self.assertRaises(ValidationError):
            cook = get_user_model().objects.create(
                username="cooktest",
                first_name="test",
                last_name="test",
                password="test123",
                years_of_experience=-1
            )

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="test")

        self.assertEqual(str(dish_type), f"{dish_type.name}")


    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(name="test")

        self.assertEqual(str(ingredient), f"{ingredient.name}")

    def test_dish_str(self):
        dish = Dish.objects.create(
            name="test",
            description="test",
            price=5,
            dish_type=DishType.objects.create(name="test")
        )

        self.assertEqual(str(dish), f"{dish.name} {dish.price}")

    def test_dish_valid_price(self):
        dish = Dish(
            name="test",
            description="test",
            price=-20,
            dish_type=DishType.objects.create(name="test")
        )

        with self.assertRaises(ValidationError):
            dish.full_clean()
