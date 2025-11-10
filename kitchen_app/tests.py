from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from kitchen_app.models import DishType, Ingredient, Dish


class ModelTests(TestCase):
    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="cooktest",
            first_name="test",
            last_name="test",
            password="test123",
            years_of_experience=5
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


class SearchFormTests(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create(
            username="cook",
            password="test123",
            years_of_experience=3)

        self.client.force_login(self.admin_user)

    def test_search_form_cooks(self):
        first_cook = get_user_model().objects.create(
            username="real",
            password="test123",
            years_of_experience=3)

        second_cook = get_user_model().objects.create(
            username="fake",
            password="test123",
            years_of_experience=4)

        url = reverse("kitchen_app:cook-list")
        response = self.client.get(url, {"name": "real"})
        results = response.context["cook_list"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(results), 1)
        self.assertIn(first_cook, results)
        self.assertNotIn(second_cook, results)

    def test_search_form_ingredients(self):
        first_ingredient = Ingredient.objects.create(name="real")
        second_ingredient = Ingredient.objects.create(name="fake")

        url = reverse("kitchen_app:ingredient-list")
        response = self.client.get(url, {"name": "real"})
        results = response.context["ingredient_list"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(results), 1)
        self.assertIn(first_ingredient, results)
        self.assertNotIn(second_ingredient, results)

    def test_search_form_dishes(self):
        first_dish = Dish.objects.create(
            name="real",
            description="real",
            price=5,
            dish_type=DishType.objects.create(name="test")
        )

        second_dish = Dish.objects.create(
            name="fake",
            description="fake",
            price=5,
            dish_type=DishType.objects.create(name="test")
        )

        url = reverse("kitchen_app:dish-list")
        response = self.client.get(url, {"name": "real"})
        results = response.context["dish_list"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(results), 1)
        self.assertIn(first_dish, results)
        self.assertNotIn(second_dish, results)
